# ROS-Action-Aruco-Marker-Pose-Estimation-wrt-Robot
ROS Action Server for Aruco marker Pose Estimation with respect to camera or robot

# Instructions
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
      
      


      
      
