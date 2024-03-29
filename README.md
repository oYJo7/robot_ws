- - -
# 2023_1_2
- - -
* 우분투 설치 20.04.5 버전 VirtualBox에 설치
    * image 주소: https://releases.ubuntu.com/focal/ 데스크탑 버전 설치
* ROS2 설치
    * foxy: sudo apt install ros-foxy-desktop ros-foxy-rmw-fastrtps* ros-foxy-rmw-cyclonedds*
* testpub testsub으로 ROS2 정상작동 확인.
* turtlesim_node 실행 후 teleop 으로 움직임 확인.
* ROS2 파이썬 패키지 만들기.
    * mpub.py 파일 코드 작성.


- - - 
# 2023_1_3
- - -
* QoS 서비스 품질.
* bashrc 의 내용 수정 띄어 쓰기 문제.
    * source /opt/ros/foxy/setup.bash source ~/robot_ws/install/local_setup.bash
        ```
        source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
        source /usr/share/vcstool-completion/vcs.bash
        source /usr/share/colcon_cd/function/colcon_cd.sh
        export _colcon_cd_root=~/robot_ws

        export ROS_DOMAIN_ID=23
        export ROS_NAMESPACE=robot1

        export RMW_IMPLEMENTATION=rmw_fastrtps_cpp
        # export RMW_IMPLEMENTATION=rmw_connext_cpp
        # export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
        # export RMW_IMPLEMENTATION=rmw_gurumdds_cpp

        # export RCUTILS_CONSOLE_OUTPUT_FORMAT='[{severity} {time}] [{name}]: {message} ({function_name}() at {file_name}:{line_number})'
        export RCUTILS_CONSOLE_OUTPUT_FORMAT='[{severity}]: {message}'
        export RCUTILS_COLORIZED_OUTPUT=1
        export RCUTILS_LOGGING_USE_STDOUT=0
        export RCUTILS_LOGGING_BUFFERED_STREAM=1

        alias cw='cd ~/robot_ws'
        alias cs='cd ~/robot_ws/src'
        alias ccd='colcon_cd'

        alias cb='cd ~/robot_ws && colcon build --symlink-install'
        alias cbs='colcon build --symlink-install'
        alias cbp='colcon build --symlink-install --packages-select'
        alias cbu='colcon build --symlink-install --packages-up-to'
        alias ct='colcon test'
        alias ctp='colcon test --packages-select'
        alias ctr='colcon test-result'
        alias sb='source ~/.bashrc'

        alias rt='ros2 topic list'
        alias re='ros2 topic echo'
        alias rn='ros2 node list'

        alias killgazebo='killall -9 gazebo & killall -9 gzserver  & killall -9 gzclient'

        alias af='ament_flake8'
        alias ac='ament_cpplint'

        alias testpub='ros2 run demo_nodes_cpp talker'
        alias testsub='ros2 run demo_nodes_cpp listener'
        alias testpubimg='ros2 run image_tools cam2image'
        alias testsubimg='ros2 run image_tools showimage'
        ```
* 1교시 메세지 퍼블리셔 섭스크라이버 작성.
* ros2 run m_pubsub mp 정상작동 확인.
* Sass 연습 google slide : https://docs.google.com/presentation/d/1jwksntFzRzFbpEtHJCzOahT5loVWIPO-PtTMm4BnxtY/edit?usp=sharing
* 코딩으로 만든 node를 통해서 turtlesim 움직이기
* ros2 run packagename command --ros-args -r __ns:=/namespacename
* ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.5, y: 7.0, theta: 1.5, name: 'turtle2'}" 터틀심 스폰 시키기
* ros2 service call /turtle1/set_pen turtlesim/srv/SetPen "{r: 100, g: 50, b: 200, width: 5}" 터틀 팬색깔, 팬두께 
* 한 화면에서 두 개의 터틀 동시에 움직이기

- - - 
# 2023_1_4
- - -
* 서비스 설명
* 서비스 코드 작성
* 인터페이스 패키지 만들기
* git 에러 해결
    ```
    find .git/objects/ -size 0 -exec rm -f {} \;
    git fetch origin
    git status
    ```
* fibonacci action 실습

- - - 
# 2023_1_5
- - -
* action code 해석
* action code flow 해석
* parameter 설명
* turtlesim 으로 parameter 연습
* launch 파일 작성과 launch 파일로 파라미터 작성하고 적용하기
    * 추가: launch 파일을 패키지에 넣어서 share 적용하는 법 - python 
    * 