cl1 = 1;
Point (1)={0.0000,0.0000,0.0000   ,  cl1};
Point (2)={0.0000,-1.0000,0.0000  ,  cl1};
Point (3)={1.0000,0.0000,0.0000   ,  cl1};
Point (4)={0.0000,1.0000,0.0000   ,  cl1};
Point (5)={-1.0000,0.0000,0.0000  ,  cl1};
Physical Point ("embedd_y") = {3, 5};
Physical Point ("embedd_x") = {4, 2};
Point (6)={-10.0000,-5.0000,0.0000,30*cl1};
Point (7)={0.0000,-5.0000,0.0000  ,10*cl1};
Point (8)={10.0000,-5.0000,0.0000 ,30*cl1};
Point (9)={10.0000,0.0000,0.0000,  30* cl1};
Point (10)={10.0000,5.0000,0.0000, 30*cl1};
Point (11)={0.0000,5.0000,0.0000,  10*cl1};
Point (12)={-10.0000,5.0000,0.0000,30*cl1};
Point (13)={-10.0000,0.0000,0.0000,30*cl1};
Circle (1)={2,1,3};
Circle (2)={3,1,4};
Circle (3)={4,1,5};
Circle (4)={5,1,2};
Line (5)={6,7};
Line (6)={7,8};
Line (7)={8,9};
Line (8)={9,10};
Physical Line ("stress") = {7,8};
Line (9)={10,11};
Line (10)={11,12};
Line (11)={12,13};
Line (12)={13,6};
Physical Line ("stress1") = {11,12};
Line (13)={2,7};
Line (14)={3,9};
Line (15)={4,11};
Line (16)={5,13};
//Physical Line ("embedd_x") = {15,13};
//Physical Line ("embedd_y") = {14,16};
Line Loop(17)={5,-13,-4,16,12};
Line Loop(18)={6,7,-14,-1,13};
Line Loop(19)={14,8,9,-15,-2};
Line Loop(20)={-16,-3,15,10,11};
Plane Surface (21)={17};
Plane Surface (22)={18};
Plane Surface (23)={19};
Plane Surface (24)={20};
Physical Surface ("sheet")={21,22,23,24};
Mesh.CharacteristicLengthFromPoints = 1;
Mesh.CharacteristicLengthFromCurvature = 1;