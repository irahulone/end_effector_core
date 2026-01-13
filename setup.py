from setuptools import find_packages, setup

package_name = 'end_effector_core'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='workcell-ee-grp1',
    maintainer_email='workcell-ee-grp1@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'electric_parallel_gripper = end_effector_core.electric_parallel_gripper:main',
        ],
    },
)
