import React, { Component } from 'react';
import { Button, Dialog, TableCell, TableRow, DialogContent } from "@mui/material";
import EditProject from './Dialog/EditProject';
import EditActivity from './Dialog/EditActivity';
import AddActivity from './Dialog/AddActivity';
import AddProjectUser from './Dialog/AddProjectUser';
import MyProjectsEntry from './MyProjectsEntry'
import WorkTimeAPI from '../API/WorkTimeAppAPI';
import MyActivitiesEntryRow from './MyActivitiesEntryRow';
import DeleteProject from './Dialog/DeleteProject';
import ProjectUserBO from '../API/ProjectUserBO';

const activities = [
    {
        name: "Use Case erstellen",
        capacity: "45h"
    },
    {
        name: "ERM Diagram",
        capacity: "10h"
    },
    {
        name: "Blabla",
        capacity: "5h"
    },
]

/**
 * Activity-Eintrag für Projekte von MyProject
 * 
 * @author [Vi Nam Le] (https://github.com/vinamle)
 */

class MyActivitiesEntry extends Component {
    constructor(props) {
        super(props);
        this.togglePopupMyProjectsEntry = this.togglePopupMyProjectsEntry.bind(this);
        this.state = {
            // activity : props.activity,
            showDialog: false,
            showPopupMyProjectEntry: false,

            projectId: props.projectId,
            activity: null,
            showWorkDialog: false,
            userId: props.userId,

            admin: props.admin,

            showAddActivity: false,
            showEditProject: false,
            showAddDialog: false,
            showDeleteProjectDialog: false,
            members:"",
            projectmember: [],
        }
    }

    addProjectUsers = (user) => {
        if (user) {
            const newProjectUserList = [...this.state.projectmember, user];
            this.setState({
              projectmember: newProjectUserList,
              showAddDialog: false
            });
          } else {
            this.setState({
              showAddDialog: false
            });
          }

      }

      getProjectMembers = () => {
        let res = []
        console.log("Projekt ID", this.state.projectId);
        WorkTimeAPI.getAPI().getMembersByProjectId(this.state.projectId).then(members =>
            this.setState({
                members: members
            }, function () {
                console.log('Hier die Members', members)
                members.forEach(elem => {
                    WorkTimeAPI.getAPI().getUserById(elem.userId).then(user =>
                        res.push(user)
                        //    this.setState({
                        //         projectmember : [...this.state.projectmember, user].filter(distinct)
                        //    }, function(){
                        //         console.log('Hier der User', user)
                        //         console.log("PROJEKTMEMBER")
                        //         res.push(user)
                        //         console.log('Hier state von ProjektMember',this.state.projectmember);
                        //    })
                    )
                });
            })
        )

        this.setState({
            projectmember: res
        }, function () {
            console.log("RES", res)
        })

        console.log('Final', this.state.projectmember)
    }

    // Aktivitäten eines Projekts holen
    getActivities = () => {
        WorkTimeAPI.getAPI().getActByProject(this.state.projectId).then(activities =>
            this.setState({
                activity: activities
            }, function () {
                console.log("Activities aus Backend", this.state.activity)
            })
        )
    }

    // Dialog öffnen
    showEdit = () => {
        this.setState({
            showWorkDialog: true
        }, function () {
            console.log("EditWindow öffnen per OnClick")
        })
    }

    // Schließen von Dialog 
    closeDialog = () => {
        this.setState({
            showWorkDialog: false
        }, function () {
            console.log("Editwindow wird geschlossen")
        })
    }

    togglePopupMyProjectsEntry() {
        this.setState({
            showPopupMyProjectEntry: !this.state.showPopupMyProjectEntry
        });
    }

    // Activities des Projects holen sobald die Komponente geladen ist
    componentDidMount() {
        this.getActivities();
        this.getProjectMembers();

    }

    // Dialog zur Bearbeitung von Projekt öffnen
    openEditProjectWindow = () => {
        this.setState({
            showEditProject: true
        }, function () {
            console.log('Edit Window Projekt öffnen')
        })
        console.log(this.state.showEditProject)
    }

    // Schließen von Dialog zur Bearbeitung von Projekt
    closeEditProjectWindow = (updatedProject) => {
        if (updatedProject){
        this.setState({
            projectId:updatedProject.getID(), 
            showEditProject: false
        }, function () {
            console.log('Edit Window Projekt schließen')
        })}
        else{
            this.setState({
                showEditProject: false
            }, function () {
                console.log('Edit Window Projekt schließen')
            })

        }
        
        this.props.onProjectEdited(updatedProject)
    }

    // Dialog zum Hinzufügen von von Aktivitäten öffnen
    openAddActivityWindow = () => {
        // if(item.userId == this.state.userId){
        //   this.setState({
        //     showAddActivity: true
        //   }, function(){
        //     console.log('Add Activity Window öffnen')
        //   })  
        //   console.log(this.state.showEditProject)
        // }else{
        //   console.log('Hallo')
        // }

        this.setState({
            showAddActivity: true
        }, function () {
            console.log('Add Activity Window öffnen')
        })
        console.log(this.state.showAddActivity)
    }

    // Dialog zum Hinzufügen von von Aktivitäten schließen
    closeAddActivityWindow = (activity) => {
        if (activity) {
            const newActivityList = [...this.state.activity, activity];
            this.setState({
                activity: newActivityList,
                showAddActivity: false
            });
        } else {
            this.setState({
                showCustomerForm: false
            });
        }
        // this.setState({
        //     showAddActivity:false
        // }, function(){
        //     console.log('Add Activity Window schließen')
        // })
    }

    openAddDialog = () => {
        this.setState({
            showAddDialog: true
        }, function () {
            console.log(this.state.showAddDialog);
        })
    }

    closeAddDialog = () => {
        this.setState({
            showAddDialog: false
        }, function () {
            console.log(this.state.showAddDialog);
        })
    }
    deleteProjectButtonClicked = () => {
        this.setState({
            showDeleteProjectDialog: true
        });
    }

    deleteProjectDialogClosed = (project) => {
        if (project) {
            this.props.onProjectDeleted(project);
        };

        // Don´t show the dialog
        this.setState({
            showDeleteProjectDialog: false
        });
    }

    activityDeleted = activity => {
        const newActivityList = this.state.activity.filter(activityFromState => activityFromState.getID() !== activity.getID());
        console.log(activity)
        this.setState({
            activity: newActivityList,
        });
    }

    projectMemberDeleted = (update) => {
        
        const newProjectMemberList = this.state.projectmember.filter(userFromState => userFromState[0].getID() !== update.getID());
        console.log("NewProjectMemberList", newProjectMemberList)
        console.log(update)
        this.setState({
          projectmember: newProjectMemberList,
        });
    }

    render() {
        const { activity, userId, admin } = this.state
        if (activity == null) {
            return null
        }
        return (
            <>
                {/* <TableRow
                    hover
                    onClick = {this.showEdit}
                >
                    <TableCell>{this.state.activity}</TableCell>
                    <TableCell>{this.state.activity}</TableCell>
                    <TableCell>
                    
                    </TableCell>
                    
                </TableRow> */}
                {/* Button für das starten von Timer  */}

                {/* <Button variant="contained" onClick={this.togglePopupMyProjectsEntry.bind(this)}>start</Button>
                    {this.state.showPopupMyProjectEntry ? 
                    <MyProjectsEntry
                    text='Close'
                    closePopup={this.togglePopupMyProjectsEntry.bind(this)}
                    user={this.state.currentUser} workTimeAccount ={this.state.workTimeAccountId}
                    />
                    : null
                    } */}


                {
                    // this.state.activity.map((elem) => (
                    //     <TableRow
                    //     hover
                    //     onClick = {this.showEdit}
                    //     >
                    //         <TableCell>{}</TableCell>
                    //         <TableCell>{}</TableCell>
                    //         {/* <TableCell></TableCell> */}
                    //     </TableRow>
                    // ))

                    activity.map((elem) => (
                        <MyActivitiesEntryRow key={elem.getID()} onActivityDeleted={this.activityDeleted} activity={elem} userId={this.state.userId}>

                        </MyActivitiesEntryRow>
                    ))

                }
                <Button onClick={this.openEditProjectWindow} disabled={admin != userId} >Edit Project</Button>
                <Button id='addActivity' onClick={this.openAddActivityWindow} disabled={admin != userId}>Add Activity</Button>
                <Button id="addProjectUser" onClick={this.openAddDialog} disabled={admin != userId}>Add Project Member</Button>
                <Button onClick={this.deleteProjectButtonClicked}disabled={admin != userId} >Delete Project</Button>

                <AddProjectUser show={this.state.showAddDialog} project={this.state.projectId} onClose={this.addProjectUsers}></AddProjectUser>
                <EditProject onProjectMemberDeleted={this.projectMemberDeleted} projectmembers={this.state.projectmember} userId={this.props.userId} name={this.props.name} commissioner={this.props.commissioner} show={this.state.showEditProject} project={this.state.projectId} onClose={this.closeEditProjectWindow}></EditProject>
                <AddActivity show={this.state.showAddActivity} project={this.state.projectId} onClose={this.closeAddActivityWindow}></AddActivity>
                <DeleteProject show={this.state.showDeleteProjectDialog} project={this.state.projectId} onClose={this.deleteProjectDialogClosed} />

            </>
        );
    }
}

export default MyActivitiesEntry;