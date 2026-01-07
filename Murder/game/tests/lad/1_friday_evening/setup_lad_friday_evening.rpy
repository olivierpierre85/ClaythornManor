label setup_lad_friday_evening_1:
    python:
        store.current_character = lad_details
        store.current_chapter = "friday_evening"
        disable_all_tutorials()
        
        # Access the 'test' store via the main store
        t = getattr(store, "test", None)
        if t:
            t.autorunner.reset()
            t.autorunner.load_plan_file("tests/lad/1_friday_evening/setup_lad_friday_evening_1.json")
            
            # Manual previous-chapter threads
            # t.unlock_threads(lad_details, ["whisky"]) TO TEST DEATH by whisky
            
            t.autorunner.target_chapter = "friday_evening"
        else:
            print("ERROR: 'test' store not found in setup_lad_friday_evening_1")

    return