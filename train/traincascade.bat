@echo %DATE% , %TIME%

opencv_traincascade.exe ^
-data cascade_ALL2_HAAR ^
-vec positive_faces.vec ^
-bg bg.txt ^
-numStages 10 ^
-featureType HAAR ^
-w 19 ^
-h 19 ^
-mode ALL

@echo %DATE% , %TIME%
Pause