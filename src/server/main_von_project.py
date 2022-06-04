from server.Businesslogic import Businesslogic
from server.bo import ProjectBO
from server.bo import ProjectUserBO
from server.bo import ActivityBO
from SecurityDecorator import secured

'''Project'''
project = api.inherit('Project', bo, {
    'name': fields.String(attribute='_name', description='Der Name des Projekts'),
    'commissioner': fields.String(attribute='_commissioner', description='Der Name des Projektleiter'),
    'user_id': fields.Integer(attribute='_user_id', description='Die ID eines Benutzer')
})

'''ProjectUser'''
projectuser = api.inherit('ProjectUser', bo, {
    'project_id': fields.Integer(attribute='_project_id', description='Die ID eines Projektmitglieds'),
    'user_id': fields.Integer(attribute='_user_id', description='Die ID eines Benutzer'),
    'capacity': fields.Float(attribute='_capacity', description='Die Kapazität eines Projekts')
})

'''Activity'''
activity = api.inherit('Activity', bo, {
    'name': fields.String(attribute='_name', description='Der Name des Projekts'),
    'capacity': fields.Float(attribute='_capacity', description='Die Kapazität eines Projekts'),
    'project_id': fields.Integer(attribute='_project_id', description='Die ID eines Projekts'),
    'duration': fields.Float(attribute='_duration', description='Die Dauer einer Aktivität')

})

#Project
@api.route('/projects')
class ProjectOperations(Resource):
    @api.marshal_with(project)
    @api.expect(project)
    @secured
    def post(self):
        adm = Businesslogic()
        proposal = ProjectBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_project(
                proposal.get_name(),
                proposal.get_commissioner(),
                proposal.get_user_id()
            )
            return p

    @api.marshal_list_with(project)
    @secured
    def get(self):
        adm = Businesslogic()
        project = adm.get_all_projects()
        return project


@api.route('/project/<int:id>')
@api.param('id', 'Die ID des Projekts')
class ProjectWithIDOperations(Resource):
    @api.marshal_with(project)
    @secured
    def get(self, id):
        adm = Businesslogic()
        project = adm.get_project_by_id(id)
        return project

    @api.marshal_with(project)
    @secured
    def get_user(self, id):
        adm = Businesslogic()
        project = adm.get_projects_by_user_id(id)
        return project

    @api.marshal_with(project)
    @secured
    def delete(self, id):
        adm = Businesslogic()
        project = adm.get_project_by_id(id)
        adm.delete_project(project)
        return ''

    @api.marshal_with(project)
    @api.expect(project, validate=True)
    @secured
    def put(self, id):
        adm = Businesslogic()
        p = ProjectBO.from_dict(api.payload)

        if p is not None:
            p.set_id(id)
            adm.update_project(p)
            return p, 200
        else:
            return '', 50
    
@api.route('/project/<str:name>')
@api.param('name', 'Der Name des Projekts')
class ProjectWithSTRINGOperations(Resource):
    @api.marshal_with(project)
    @secured
    def get(self, name):
        adm = Businesslogic()
        activity = adm.get_by_project_name(name)
        return activity


#ProjectUser
@api.route('/projectusers')
class ProjectUserOperations(Resource):
    @api.marshal_with(projectuser)
    @api.expect(projectuser)
    @secured
    def post(self):
        adm = Businesslogic()
        proposal = ProjectUserBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_projectuser(
                proposal.get_project_id(),
                proposal.get_user_id(),
                proposal.get_capacity()
            )
            return p

    @api.marshal_list_with(projectuser)
    @secured
    def get(self):
        adm = Businesslogic()
        projectuser = adm.get_all_projectusers()
        return projectuser


@api.route('/projectuser/<int:id>')
@api.param('id', 'Die ID des Projekts')
class ProjectWithIDOperations(Resource):
    @api.marshal_with(projectuser)
    @secured
    def get(self, id):
        adm = Businesslogic()
        projectuser = adm.get_projectuser_by_id(id)
        return projectuser

    def get_project_members(self, project_id):
        adm = Businesslogic()
        projectuser = adm.get_all_project_members(project_id)
        return projectuser

    @api.marshal_with(projectuser)
    @secured
    def delete(self, id):
        adm = Businesslogic()
        projectuser = adm.get_projectuser_by_id(id)
        adm.delete_projectuser(projectuser)
        return ''

    @api.marshal_with(projectuser)
    @api.expect(projectuser, validate=True)
    @secured
    def put(self, id):
        adm = Businesslogic()
        p = ProjectUserBO.from_dict(api.payload)

        if p is not None:
            p.set_id(id)
            adm.update_projectuser(p)
            return p, 200
        else:
            return '', 500

#Activity
@api.route('/activities')
class ActivityOperations(Resource):
    @api.marshal_with(activity)
    @api.expect(activity)
    @secured
    def post(self):
        adm = Businesslogic()
        proposal = ActivityBO.from_dict(api.payload)
        if proposal is not None:
            p = adm.create_project(
                proposal.get_name(),
                proposal.get_capacity(),
                proposal.get_project_id(),
                proposal.get_duration()
            )
            return p

    @api.marshal_list_with(activity)
    @secured
    def get(self):
        adm = Businesslogic()
        activity = adm.get_all_activities()
        return activity


@api.route('/activity/<int:id>')
@api.param('id', 'Die ID der Aktivitaet')
class ActivityWithIDOperations(Resource):
    @api.marshal_with(activity)
    @secured
    def get(self, id):
        adm = Businesslogic()
        activity = adm.get_activity_by_id(id)
        return activity

    def get_project_id(self, id):
        adm = Businesslogic()
        activity = adm.get_all_by_project_id(id)
        return activity

    @api.marshal_with(activity)
    @secured
    def delete(self, id):
        adm = Businesslogic()
        activity = adm.get_activity_by_id(id)
        adm.delete_activity(activity)
        return ''

    @api.marshal_with(activity)
    @api.expect(activity, validate=True)
    @secured
    def put(self, id):
        adm = Businesslogic()
        p = ActivityBO.from_dict(api.payload)

        if p is not None:
            p.set_id(id)
            adm.update_activity(p)
            return p, 200
        else:
            return '', 500

@api.route('/activity/<str:name>')
@api.param('name', 'Der Name der Aktivitaet')
class ActivityWithSTRINGOperations(Resource):
    @api.marshal_with(activity)
    @secured
    def get(self, name):
        adm = Businesslogic()
        activity = adm.get_by_name(name)
        return activity