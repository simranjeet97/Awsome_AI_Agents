# Extended Weather Formatting Guide

## For forecast requests (multi-day)
Present as a table:
| Day  | High | Low  | Condition     |
|------|------|------|---------------|
| Mon  | 28°C | 19°C | Partly cloudy |

## For severe weather
Always lead with a ⚠️ warning before the weather data and recommend
appropriate precautions (umbrella, avoiding travel, etc.).

## Units reference
- Default: Celsius (°C), wind in km/h, precipitation in mm
- If the user mentions "imperial", switch to: Fahrenheit (°F), mph, inches
- If the user is clearly from the US (mentions US cities), offer both units
