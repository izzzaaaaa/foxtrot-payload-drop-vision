# Test Log

## Lighting Conditions

| Date | Condition | Observation | HSV Behavior |
|------|-----------|-------------|---------------|
| 25-7-2026 | Direct light on marker | Marker appeared near white | Saturation dropped sharply toward 0. Hue became inconsistent even though it was the same physical object |

## Mask Quality / Noise Cleanup

| Date | Stage | Observation |
|------|-------|-------------|
| 26-7-2026 | Raw mask (before erosion/dilation) | Mask was already quite clean with calibrated HSV range and minimal background noise |
| 27-7-2026 | After erosion/dilation (opening +closing) | Removed a few stray pixels near edges |