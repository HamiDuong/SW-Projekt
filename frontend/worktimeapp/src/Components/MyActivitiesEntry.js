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
            
            projectId : props.projectId,
            activity : null,
            showWorkDialog: false,
            userId: props.userId,

            admin : props.admin,

            showAddActivity: false,
            showEditProject: false,
            showAddDialog: false,
            showDeleteProjectDialog: false
        }
    }

    // Aktivitäten eines Projekts holen
    getActivities = () => {
        WorkTimeAPI.getAPI().getActByProject(this.state.projectId).then( activities =>
            this.setState({
                activity : activities
            }, function(){
                console.log("Activities aus Backend", this.state.activity)
            })
        )
    }

    // Dialog öffnen
    showEdit = () => {
        this.setState({
            showWorkDialog: true
        }, function(){
            console.log("EditWindow öffnen per OnClick")
        })
    }

    // Schließen von Dialog 
    closeDialog = () => {
        this.setState({
            showWorkDialog: false
        }, function(){
            console.log("Editwindow wird geschlossen")
        })
    }

    togglePopupMyProjectsEntry() {
        this.setState({
          showPopupMyProjectEntry: !this.state.showPopupMyProjectEntry
        });
    }

    // Activities des Projects holen sobald die Komponente geladen ist
    componentDidMount(){
        this.getActivities();
    }

    // Dialog zur Bearbeitung von Projekt öffnen
    openEditProjectWindow = () => {
        this.setState({
          showEditProject: true
        }, function(){
          console.log('Edit Window Projekt öffnen')
        })
        console.log(this.state.showEditProject)
    }
    
    // Schließen von Dialog zur Bearbeitung von Projekt
    closeEditProjectWindow = () => {
        this.setState({
            showEditProject:false
        }, function(){
            console.log('Edit Window Projekt schließen')
        })
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
          }, function(){
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
            showAddDialog : true
        }, function(){
            console.log(this.state.showAddDialog);
        })
    }

    closeAddDialog = () => {
        this.setState({
            showAddDialog : false
        }, function(){
            console.log(this.state.showAddDialog);
        })
    }
    deleteProjectButtonClicked = () => {
        this.setState({
          showDeleteProjectDialog: true
        });
      }

    deleteProjectDialogClosed= (project) => {
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
    
    render() { 
        const {activity, userId, admin} = this.state 
        if(activity ==  null) {
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
                        <MyActivitiesEntryRow key={elem.getID()} onActivityDeleted={this.activityDeleted} activity = {elem} userId = {this.state.userId}>

                        </MyActivitiesEntryRow>
                    ))
                    
                }
                <Button onClick = {this.openEditProjectWindow} show = {admin != userId}>Edit Project</Button>
                <Button id = 'addActivity' onClick = {this.openAddActivityWindow} show = {admin != userId}>Add Activity</Button>
                <Button id = "addProjectUser" onClick = {this.openAddDialog} show = {admin != userId}>Add Project Member</Button>
                <Button onClick={this.deleteProjectButtonClicked} show = {admin != userId}>Delete Project</Button>
                
                <AddProjectUser show = {this.state.showAddDialog} project = {this.state.projectId} onClose = {this.closeAddDialog}></AddProjectUser>
                <EditProject show={this.state.showEditProject} project = {this.state.projectId} onClose={this.closeEditProjectWindow}></EditProject>
                <AddActivity show = {this.state.showAddActivity} project = {this.state.projectId} onClose = {this.closeAddActivityWindow}></AddActivity>
                <DeleteProject show={this.state.showDeleteProjectDialog} project={this.state.projectId} onClose={this.deleteProjectDialogClosed} />

            </>
        );
    }
}
 
export default MyActivitiesEntry;