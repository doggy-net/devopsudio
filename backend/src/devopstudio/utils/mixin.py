def dict_mixin(target, update):
    if not isinstance(target, dict) or not isinstance(update, dict):
        return
    for key in update:
        if isinstance(update[key], dict):
            dict_mixin(target[key], update[key])
        else:
            target[key] = update[key]
