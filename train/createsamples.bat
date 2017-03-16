@echo %DATE% , %TIME%

opencv_createsamples.exe ^
-info info.dat ^
-vec positive_faces.vec ^
-w 19 ^
-h 19 ^
-num 2429
@echo %DATE% , %TIME%
Pause