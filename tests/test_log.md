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

## Contour Detection

| Date | Test | Result |
|------|------|--------|
| 28-7-2026 | Normal distance | Area 5560, clean detection, no background noise |
| 28-7-2026 | distance test result | Drops below 800 min area distance at around one arm's length |
| 28-7-2026 | similar color object test result | Box still locks onto correct marker as long as it is larger than second introduced marker |
| 28-7-2026 | Covering test result | Contour still gets picked up with the area decreasing  |

## Drop Trigger

| Date | Test | Result |
|------|------|--------|
| 30-7-2026 | Marker moved to frame center | "DROP TRIGGERED" printed correctly, vehicle mode confirmed as stabilized |

## Drop-Trigger Accuracy Log

TOLERANCE = 20px | Frame center: (320, 240) | Frame res: 640x480

| Trial | Intended Position | Classification |
|-------|-------------------|----------------|
| 1 | Centered(by eye) | DROP TRIGGERED - True Positive |
| 2 | Centered (by eye) | DROP TRIGGERED - True Positive |
| 3 | Clearly off-center (left/right) | Not aligned - True Negative |
| 4 | Clearly off-center (up/down) | Not aligned - True Negative |
| 5 | Near tolerance edge (offset_x hovering 19-20) | Alternated between "Not aligned" and "DROP TRIGGERED" without deliberate marker movement - likely False Positives, since intended position was borderline |
