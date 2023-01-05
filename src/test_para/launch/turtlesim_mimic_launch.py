from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(        
        [Node(
            package='turtlesim',
            namespace='ns1',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='turtlesim',
            namespace='ns2',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='mimic',
            remapping=[
                ('/input/pose', 'ns1/turtle1/pose'),
                ('/output/cmd_vel', 'ns2/turtle1/cmd_vel')
            ]
        )]
    )