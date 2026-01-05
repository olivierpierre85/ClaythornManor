label setup_lad_friday_evening_1:
    python:
        store.export_transcript_activated = True
        store.current_character = lad_details
        store.current_chapter = "friday_afternoon"
        
        # Access the 'test' store via the main store
        t = getattr(store, "test", None)
        if t:
            t.autorunner.reset()
            t.autorunner.load_plan_file("choices_anon_2025-10-01_11-00-29.json")
            
            # Manual previous-chapter threads
            t.unlock_threads(lad_details, ["whisky"])
            
            t.autorunner.target_chapter = "friday_evening"
        else:
            print("ERROR: 'test' store not found in setup_lad_friday_evening_1")

    return