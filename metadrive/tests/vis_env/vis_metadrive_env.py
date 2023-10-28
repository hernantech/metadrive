from metadrive.envs.metadrive_env import MetaDriveEnv
from metadrive.utils import setup_logger

if __name__ == "__main__":
    setup_logger(True)
    env = MetaDriveEnv(
        {
            "num_scenarios": 10,
            "traffic_density": 0,
            "start_seed": 74,
            # "_disable_detector_mask":True,
            # "debug_physics_world": True,
            "debug": False,
            # "global_light": False,
            # "debug_static_world": True,
            "pstats": True,
            "static_traffic_object": False,
            "show_interface": True,
            "random_agent_model": True,
            "cull_scene": False,
            "random_spawn_lane_index": False,
            "random_lane_width": False,
            # "image_observation": True,
            # "controller": "joystick",
            # "show_coordinates": True,
            # "random_agent_model": False,
            "manual_control": True,
            "use_render": True,
            "plane_terrain": False,
            "accident_prob": 1,
            "decision_repeat": 5,
            "daytime": "19:00",
            "interface_panel": [],
            "need_inverse_traffic": False,
            "rgb_clip": True,
            "map": "CX",
            # "agent_policy": ExpertPolicy,
            "random_traffic": False,
            # "random_lane_width": True,
            "driving_reward": 1.0,
            # "pstats": True,
            "force_destroy": False,
            # "show_terrain"
            # "show_skybox": False,
            "show_fps": False,
            "render_pipeline": True,
            # "camera_dist": 8,
            "window_size": (1200, 800),
            "camera_dist": 13,
            # "camera_pitch": 30,
            "camera_height": 3,
            # "camera_smooth": False,
            # "camera_height": -1,
            "vehicle_config": {
                "enable_reverse": True,
                # "vehicle_model": "xl",
                # "rgb_camera": (1024, 1024),
                # "spawn_velocity": [8.728615581032535, -0.24411703918728195],
                "spawn_velocity_car_frame": True,
                # "image_source": "depth_camera",
                # "random_color": True
                # "show_lidar": True,
                "spawn_lane_index": None,
                # "destination":"2R1_3_",
                # "show_side_detector": True,
                # "show_lane_line_detector": True,
                # "side_detector": dict(num_lasers=2, distance=50),
                # "lane_line_detector": dict(num_lasers=2, distance=50),
                # "show_line_to_navi_mark": True,
                "show_navi_mark": False,
                # "show_dest_mark": True
            },
        }
    )
    import time

    speed = 8

    def acc_speed():
        global speed
        speed *= 2

    def de_speed():
        global speed
        speed /= 2

    def lower_terrain():
        pos = env.engine.terrain._mesh_terrain.getPos()
        env.engine.terrain._mesh_terrain.set_pos(pos[0], pos[1], pos[2] - speed)

    def lift_terrain():
        pos = env.engine.terrain._mesh_terrain.getPos()
        env.engine.terrain._mesh_terrain.set_pos(pos[0], pos[1], pos[2] + speed)

    init_state = {
        'position': (40.82264362985734, -509.3641208712943),
        'heading': -89.41878393159747,
        'velocity': [8.728615581032535, -0.24411703918728195],
        'valid': True
    }

    start = time.time()

    o, _ = env.reset()
    env.engine.accept("~", env.engine.terrain.reload_terrain_shader)
    if env.config["render_pipeline"]:
        env.engine.accept("5", env.engine.render_pipeline.reload_shaders)
        env.engine.accept("7", acc_speed)
        env.engine.accept("8", de_speed)
        env.engine.accept("9", lift_terrain)
        env.engine.accept("0", lower_terrain)
    env.engine.accept("`", env.engine.terrain.reload_terrain_shader)
    # env.main_camera.set_follow_lane(True)
    # env.vehicle.get_camera("rgb_camera").save_image(env.vehicle)
    # for line in env.engine.coordinate_line:
    #     line.reparentTo(env.vehicle.origin)
    # env.vehicle.set_velocity([5, 0], in_local_frame=True)
    print(time.time() - start)
    for s in range(1, 100000):
        # env.vehicle.set_velocity([1, 0], in_local_frame=True)
        o, r, tm, tc, info = env.step([0, 0])
        # if tm:
        #     s = time.time()
        #     env.reset()
        #     print(time.time() - s)

        # env.vehicle.set_pitch(-np.pi/4)
        # [0.09231533, 0.491018, 0.47076905, 0.7691619, 0.5, 0.5, 1.0, 0.0, 0.48037243, 0.8904728, 0.81229943, 0.7317231, 1.0, 0.85320455, 0.9747932, 0.65675277, 0.0, 0.5, 0.5]
        # else:
        # if s % 100 == 0:
        #     env.close()
        #     env.reset()
        # info["fuel"] = env.vehicle.energy_consumption
        # env.render(
        #     text={
        #         # "heading_diff": env.vehicle.heading_diff(env.vehicle.lane),
        #         # "lane_width": env.vehicle.lane.width,
        #         # "lane_index": env.vehicle.lane_index,
        #         # "lateral": env.vehicle.lane.local_coordinates(env.vehicle.position),
        #         "current_seed": env.current_seed
        #     }
        # )
        # if tm or tc:
        #     env.reset()
        # # assert env.observation_space.contains(o)
        # if (s + 1) % 100 == 0:
        #     # print(
        #         "Finish {}/10000 simulation steps. Time elapse: {:.4f}. Average FPS: {:.4f}".format(
        #             s + 1,f
        #             time.time() - start, (s + 1) / (time.time() - start)
        #         )
        #     )
        # if tm or tc:
        # #     # env.close()
        # #     # print(len(env.engine._spawned_objects))
        # env.reset()
# [0.09231525, 0.4910181, 0.470769, 0.7691619, 0.5, 0.5, 1.0, 0.0, 0.4803721,

# 0.81229913, 0.8904725, 0.7317231, 1.0, 0.85320455,
# 0.6567526, 0.9747927, 0.0, 0.5, 0.5]
