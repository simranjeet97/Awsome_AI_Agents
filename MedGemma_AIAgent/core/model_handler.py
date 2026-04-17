import torch
from transformers import AutoProcessor, AutoModelForImageTextToText, BitsAndBytesConfig
import os

class MedGemmaHandler:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MedGemmaHandler, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def initialize(self, model_id="google/medgemma-1.5-4b-it", use_quantization=True, hf_token=None):
        if self.initialized:
            return
        
        self.model_id = model_id
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        if hf_token:
            os.environ["HF_TOKEN"] = hf_token

        try:
            # 1. Load Processor
            self.processor = AutoProcessor.from_pretrained(self.model_id)

            # 2. Configure Quantization if on CUDA
            bnb_config = None
            if use_quantization and self.device == "cuda":
                bnb_config = BitsAndBytesConfig(
                    load_in_4bit=True,
                    bnb_4bit_compute_dtype=torch.bfloat16,
                    bnb_4bit_quant_type="nf4",
                    bnb_4bit_use_double_quant=True,
                )

            # 3. Load Model
            self.model = AutoModelForImageTextToText.from_pretrained(
                self.model_id,
                torch_dtype=torch.bfloat16 if self.device == "cuda" else torch.float32,
                quantization_config=bnb_config,
                device_map="auto" if self.device == "cuda" else None
            )
            
            if self.device == "cpu":
                self.model.to(self.device)

            self.initialized = True
            print(f"Model {model_id} loaded successfully on {self.device}")
        except Exception as e:
            print(f"Error loading model: {e}")
            self.initialized = False
            raise e

    def analyze(self, images, prompt="Analyze this medical scan and list key findings.", max_new_tokens=1024):
        """
        Inference call for MedGemma.
        'images' can be a single PIL Image or a list of PIL Images.
        """
        if not self.initialized:
            return "Model not initialized."

        # Prepare messages for multimodal template
        if not isinstance(images, list):
            images = [images]

        content = []
        for img in images:
            content.append({"type": "image", "image": img})
        content.append({"type": "text", "text": prompt})

        messages = [
            {
                "role": "user",
                "content": content
            }
        ]

        inputs = self.processor.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt"
        ).to(self.model.device, dtype=torch.bfloat16 if self.device == "cuda" else torch.float32)

        input_len = inputs["input_ids"].shape[-1]

        with torch.inference_mode():
            generation = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False # Greedy decoding as per latest recommendations
            )
            generation = generation[0][input_len:]
            
        decoded = self.processor.decode(generation, skip_special_tokens=True)
        return decoded

    def mock_analyze(self, scan_type="CT"):
        """Fallback for testing UI without model weights."""
        return f"### AI Analysis Report ({scan_type})\n\n**Findings:**\n- No significant abnormalities detected in the immediate viewing area.\n- Spatial alignment looks normal.\n- Tissue density indicates consistent HU values.\n\n**Clinical Recommendation:**\nCorrelation with patient history is suggested. This is a mock analysis for UI demonstration."
