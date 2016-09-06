__author__ = 'sp41mer'
from flask import Flask, render_template, request, jsonify
from models import Profile, Friendship
import peewee

app = Flask(__name__)

@app.route('/follow')
def give_follow_data():
     return render_template('follow_dynamics.html')

@app.route('/unfollow')
def give_unfollow_data():
     return render_template('unfollow_dynamics.html')

@app.route('/profile')
def give_profile_data():
     return render_template('profile_dynamics.html')

@app.route('/getdata', methods=['POST'])
def give_data():
    type = request.values['type']
    database = peewee.PostgresqlDatabase(
                    'instagram',
                    user='root',
                    password='root',
                    host='localhost'
                )
    dates = []
    values = []
    bg_colors = []
    border_colors = []
    if type == 'profile_statistic':
        for item in reversed(Profile.select().order_by(Profile.id.desc()).limit(10)):
            dates.append(item.date)
            values.append(item.count)
            border_colors.append('rgba(255,99,132,1)')
            bg_colors.append('rgba(54, 162, 235, 0.2)')
        response = {
            'success': 'OK',
            'dates': dates,
            'values': values,
            'bg_colors': bg_colors,
            "border_colors": border_colors
        }
    elif type == 'unfollow_statistic':
        for item in reversed(Friendship.select().order_by(Friendship.id.desc()).limit(10)):
            dates.append(item.date)
            values.append(item.unfollowed_counter)
            border_colors.append('rgba(255,99,132,1)')
            bg_colors.append('rgba(54, 162, 235, 0.2)')
        response = {
            'success': 'OK',
            'dates': dates,
            'values': values,
            'bg_colors': bg_colors,
            "border_colors": border_colors
        }
    elif type == 'follow_statistic':
        for item in reversed(Friendship.select().order_by(Friendship.id.desc()).limit(10)):
            dates.append(item.date)
            values.append(item.followed_counter)
            border_colors.append('rgba(255,99,132,1)')
            bg_colors.append('rgba(54, 162, 235, 0.2)')
        response = {
            'success': 'OK',
            'dates': dates,
            'values': values,
            'bg_colors': bg_colors,
            "border_colors": border_colors
        }
    else:
        response = {
            'success': 'Not OK :('
        }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)