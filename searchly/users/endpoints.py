from flask.ext.restful import abort, Resource, reqparse
from werkzeug.exceptions import ClientDisconnected
from searchly.search.readyforce import name_member_search


parser = reqparse.RequestParser()
parser.add_argument('name', type=str, location='args')


class Users(Resource):

    def get(self):
        try:
            args = parser.parse_args()
        except ClientDisconnected as e:
            abort(400, message='Query info is not valid')
        name = args.get('name')
        if not name:
            abort(400, message='No name search query provided')
        try:
            members = name_member_search(name)
        except:
            abort(400, message='Error fetching name query results')
        members_response = []
        for member in members:
            name = member.get('name')
            photo_url = member.get('photo_url')
            description = member.get('description')[:50]
            if description:
                description += '...'
            skills = member.get('skill')

            #parse and add skills
            more_skills = member.get('skill_more_values')
            if more_skills:
                skills += more_skills
            skills_string = ''

            #Pass over member if no name or photo
            if not (name and photo_url):
                continue

            #Pass back skills as a string
            if skills:
                for skill in skills:
                    skills_string += ', ' + skill.get('name')
            skills_string = skills_string[2:]
            members_response.append({
                'name': name,
                'photoUrl': photo_url,
                'skills': skills_string,
                'description': description,
            })
        return members_response
