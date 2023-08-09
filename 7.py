a_h, a_min, a_sec = (int(item) for item in input().strip().split(sep=":"))
b_h, b_min, b_sec = (int(item) for item in input().strip().split(sep=":"))
c_h, c_min, c_sec = (int(item) for item in input().strip().split(sep=":"))

def get_total_sec(h, min, sec):
    return h*60*60 + min*60 + sec

def round(number):
    if int(number) == int(number + 0.5):
        return int(number)
    else:
        return int(number) + 1

a_total_sec = get_total_sec(a_h, a_min, a_sec)
b_total_sec = get_total_sec(b_h, b_min, b_sec)
c_total_sec = get_total_sec(c_h, c_min, c_sec)

if c_total_sec < a_total_sec:
    c_total_sec += 24*60*60

additional_time = round((c_total_sec - a_total_sec) / 2)
setted_time_in_seconds = b_total_sec + additional_time

setted_sec = setted_time_in_seconds % 60
setted_min = round((setted_time_in_seconds - setted_sec) / 60) % 60
setted_h = round((setted_time_in_seconds - setted_sec - setted_min*60) / (60 * 60)) % 24

print(f"{setted_h:02}:{setted_min:02}:{setted_sec:02}")

