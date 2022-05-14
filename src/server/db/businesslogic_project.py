from bo.ProjectBO import ProjectBO
from db.ProjectMapper import ProjectMapper
from bo.ProjectUserBO import ProjectUserBO
from db.ProjectUserMapper import ProjectUserMapper
from bo.ActivityBO import ActivityBO
from db.ActivityMapper import ActivityMapper
#Project
def create_project(self, name, commissioner, user_id):
    project = ProjectBO()
    project.set_name(name)
    project.set_commissioner(commissioner)
    project.set_user_id(user_id)
    with ProjectMapper() as mapper:
        return mapper.insert(project)

def get_project_by_id(self, id):
    with ProjectMapper() as mapper:
        return mapper.find_by_key(id)

def get_all_projects(self):
    with ProjectMapper() as mapper:
        return mapper.find_all()

def save_project(self, project):
    with ProjectMapper() as mapper:
        mapper.update(project)

def delete_project(self, project):
    with ProjectMapper() as mapper:
         mapper.delete(project)

def get_projects_by_user_id(self, id):
    with ProjectMapper() as mapper:
        mapper.find_projects_by_user_id(id)

def get_by_project_name(self, name):
    with ProjectMapper() as mapper:
        mapper.find_by_project_name(name)

#Projectuser
def create_projectuser(self, project_id, user_id, capacity):
    projectuser = ProjectUserBO()
    projectuser.set_project_id(project_id)
    projectuser.set_user_id(user_id)
    projectuser.set_capacity(capacity)
    with ProjectUserMapper() as mapper:
        return mapper.insert(projectuser)

def get_projectuser_by_id(self, id):
    with ProjectUserMapper() as mapper:
        return mapper.find_by_key(id)

def get_all_projectusers(self):
    with ProjectUserMapper() as mapper:
        return mapper.find_all()

def save_projectuser(self, projectuser):
    with ProjectUserMapper() as mapper:
        mapper.update(projectuser)

def delete_projectuser(self, projectuser):
    with ProjectUserMapper() as mapper:
         mapper.delete(projectuser)
        
def get_all_project_members(self, project_id):
    with ProjectUserMapper() as mapper:
        mapper.find_all_project_members(project_id)

#Activity
def create_activity(self, name, capacity, project_id, duration):
    activity = ActivityBO()
    activity.set_name(name)
    activity.set_capacity(capacity)
    activity.set_project_id(project_id)
    activity.set_duration(duration)
    with ActivityMapper() as mapper:
        return mapper.insert(activity)

def get_activity_by_id(self, id):
    with ActivityMapper() as mapper:
        return mapper.find_by_key(id)

def get_all_activities(self):
    with ActivityMapper() as mapper:
        return mapper.find_all()

def save_activity(self, activity):
    with ActivityMapper() as mapper:
        mapper.update(activity)

def delete_activity(self, activity):
    with ActivityMapper() as mapper:
         mapper.delete(activity)

def get_by_name(self, name):
    with ActivityMapper() as mapper:
        return mapper.find_by_name(name)

def get_all_by_project_id(self, project_id):
    with ActivityMapper() as mapper:
        return mapper.find_all_by_project_id(project_id)