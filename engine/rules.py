def gesture_mapping(gesture_name):
    gesture_dict = {
        "Collect":"INCLUSIVITY",
        "Cycle":"PROCESS_CYCLE",
        "Container":"SURROUND",
        "Oscillation":"UNCERTAINTY",
        "Negation":"NEGATION",
        "Offer":"OFFER",
        "Beat":"RHYTHM"
    }
    try:
        return gesture_dict[gesture_name]
    except:
        return "" ###handle this later please thanks <3