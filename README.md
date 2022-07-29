# ROS-Action-Aruco-Marker-Pose-Estimation-wrt-Robot
ROS Action Server for Aruco marker Pose Estimation with respect to camera or robot

## Instructions
1. Create a ros workspace using mkdir catkin_ws/src.
2. Clone the all this packages in your catkin_ws/src folder using this command on terminal:

    ```console
    git clone https://github.com/Robo-Dude/ROS-Action-Aruco-Marker-Pose-Estimation-wrt-Robot.git
    ```
    
3. Go back to catkin_ws folder open the terminal run catkin_make for building code in a catkin workspace.
    ```console
    catkin_make
    ```
4. Camera Calibrating for tracking the Aruco marker:

   4.1: Open the Terminal 1 and run the ROS Master
     ```console
     roscore
     ```
   4.2: Terminal 2
      ```console
      rosrun usb_cam usb_cam_node
      ```
   4.3: Terminal 3
      ```console
      rosrun camera_calibration cameracalibrator.py --size 7x7 --square 0.02517 image:=/usb_cam/image_raw camera:=/usb_cam --no-service-check
      ```
      
      Download this Chess Board Image and take a printout, use it to calibrate the camera and generate the yaml file.
      
      https://images.app.goo.gl/MWwGHijer5Ya59428
      
      Images for reference:
      
      ![calibrate](https://user-images.githubusercontent.com/65345575/181817959-eebe7419-9112-4337-8021-aed73cc43f3e.png)
      
      roll, skew the image to get done the calibration, once the required images files get capture, you will get a option to calibrate, save and commit it
      click on calibrate , Save and then commit to save the generated yaml file at:
      
      /home/<username>/.ros/camera_info/head_camera.yaml
      
5. Now, you are ready to launch the roslaunch files.
     
    ```console
    roslaunch aruco_pose usb_cam_stream_publisher.launch 
    ```
    
    ```console
    roslaunch aruco_pose aruco_marker_finder.launch 
    ```
    
    Aruco Marker Detail:
    Marker Id: 701
    Original Aruco Marker
    
    Image - 
    
    ![aruco-701](https://user-images.githubusercontent.com/65345575/181822793-bd5ff240-95e4-4912-a3fa-15c0edb93a50.svg)
    
    Demo Video:
    
    [aruco.webm](https://user-images.githubusercontent.com/65345575/181823580-8a95776a-860d-42a0-a464-22f13a6d2833.webm)
    
    OUTPUT -
    
    x , y, Theta with respect to Robot.
    
    TO STUDY MORE VISIT THIS LINKS -
    
    https://www.researchgate.net/publication/270107591_Visual_Localization_of_Mobile_Robot_Using_Artificial_Markers
    
    https://ros-developer.com/2017/04/23/aruco-ros/
    
    https://ros-developer.com/2017/04/23/camera-calibration-with-ros/

    
    
    
    

    

    

    
      


      
      
