import sys

def main(dict):
    alerts = []

    # activity-room
    if dict['room'] == 'activity-room':
        if dict['values']['co2'] > 500:
            alerts.append('co2')

        if dict['values']['temperature'] < 19 or dict['values']['temperature'] > 22:
            alerts.append('temperature')

        if dict['values']['humidity'] < 50 or dict['values']['humidity'] > 60:
            alerts.append('humidity')

        if dict['values']['sound'] < 0 or dict['values']['sound'] > 40:
            alerts.append('sound')

        if dict['values']['illumination'] < 300 or dict['values']['illumination'] > 750:
            alerts.append('illumination')

    # refectory
    elif dict['room'] == 'refectory':
        if dict['values']['co2'] > 400:
            alerts.append('co2')

        if dict['values']['temperature'] < 20 or dict['values']['temperature'] > 23:
            alerts.append('temperature')

        if dict['values']['humidity'] < 50 or dict['values']['humidity'] > 70:
            alerts.append('humidity')

        if dict['values']['sound'] < 20 or dict['values']['sound'] > 35:
            alerts.append('sound')

        if dict['values']['illumination'] < 200 or dict['values']['illumination'] > 500:
            alerts.append('illumination')

    # room-1
    elif dict['room'] == 'room-1':
        if dict['values']['co2'] > 300:
            alerts.append('co2')

        if dict['values']['temperature'] < 21 or dict['values']['temperature'] > 23:
            alerts.append('temperature')

        if dict['values']['humidity'] < 50 or dict['values']['humidity'] > 60:
            alerts.append('humidity')

        if dict['values']['sound'] < 10 or dict['values']['sound'] > 30:
            alerts.append('sound')

        if dict['values']['illumination'] < 100 or dict['values']['illumination'] > 200:
            alerts.append('illumination')

    # bathroom-main
    elif dict['room'] == 'bathroom-main':
        if dict['values']['co2'] > 500:
            alerts.append('co2')

        if dict['values']['temperature'] < 22 or dict['values']['temperature'] > 25:
            alerts.append('temperature')

        if dict['values']['humidity'] < 60 or dict['values']['humidity'] > 75:
            alerts.append('humidity')

        if dict['values']['sound'] < 20 or dict['values']['sound'] > 35:
            alerts.append('sound')

        if dict['values']['illumination'] < 100 or dict['values']['illumination'] > 200:
            alerts.append('illumination')

    # garden
    elif dict['room'] == 'garden':
        if dict['values']['co2'] > 500:
            alerts.append('co2')

        if dict['values']['temperature'] < 15 or dict['values']['temperature'] > 22:
            alerts.append('temperature')

        if dict['values']['humidity'] < 50 or dict['values']['humidity'] > 80:
            alerts.append('humidity')

        if dict['values']['sound'] < 10 or dict['values']['sound'] > 35:
            alerts.append('sound')

    return {'alerts': alerts}