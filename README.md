# Foxtrot — Payload Drop / Landing Marker Detection

Vision system that detects a colored landing marker in a video feed, computes its centroid
`(Cx, Cy)` in real time, and passes that data to a simulated DroneKit/SITL script that logs a
`DROP` event when the marker is centered in frame.

> **Note:** This is a simulation project. No real flight or physical payload release is performed.
> Everything runs against a Software-In-The-Loop (SITL) vehicle connected via Mission Planner.

## Objective

Build an end-to-end pipeline: camera feed → HSV masking → contour detection → centroid calculation → alignment check → simulated drop trigger.

## Deliverables Checklist

**Functional**
- [ ] HSV calibration tool/trackbar script
- [ ] Mask + noise-cleanup pipeline (before/after screenshots)
- [ ] Contour detection isolating only the marker
- [ ] Real-time centroid overlay (crosshair + Cx, Cy printed on screen)
- [ ] Centroid offset converted into velocity/position correction commands sent to SITL
- [ ] DroneKit script connected to SITL, receives (Cx, Cy), logs DROP when centered

**Testing**
- [ ] Test log: performance under lighting variation, marker distance, partial occlusion,
      multiple similar-colored objects
- [ ] Drop-trigger accuracy log: correct DROP fires vs. false positives/negatives

