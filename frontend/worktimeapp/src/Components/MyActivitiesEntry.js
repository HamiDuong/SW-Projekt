import React, { Component } from 'react';
import { Button, Dialog, TableCell, TableRow, DialogContent } from "@mui/material";
import EditActivity from './Dialog/EditActivity';
import MyProjectsEntry from './MyProjectsEntry'
import WorkTimeAPI from '../API/WorkTimeAppAPI';

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
        }
    }

    getActivities = () => {
        WorkTimeAPI.getAPI().getActByProject(this.state.projectId).then( activities =>
            this.setState({
                activity : activities
            }, function(){
                console.log("Activities aus Backend", this.state.activity)
            })
        )
    }

    showEdit = () => {
        this.setState({
            showWorkDialog: true
        }, function(){
            console.log("EditWindow öffnen per OnClick")
        })
    }
    togglePopupMyProjectsEntry() {
        this.setState({
          showPopupMyProjectEntry: !this.state.showPopupMyProjectEntry
        });
      }

    closeDialog = () => {
        this.setState({
            showWorkDialog: false
        }, function(){
            console.log("Editwindow wird geschlossen")
        })
    }

    componentDidMount(){
        this.getActivities();
    }
    
    render() { 
        const {activity} = this.state 
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
                        <>
                            <TableRow
                            hover
                            onClick = {this.showEdit}
                            >
                                <TableCell>{elem.name}</TableCell>
                                <TableCell>{elem.capacity}</TableCell>
                                <TableCell>
                                    <Button variant="contained" onClick={this.togglePopupMyProjectsEntry.bind(this)}>start</Button>
                                    {this.state.showPopupMyProjectEntry ? 
                                    <MyProjectsEntry
                                    text='Close'
                                    closePopup={this.togglePopupMyProjectsEntry.bind(this)}
                                    // user={this.state.currentUser} workTimeAccount = {this.state.workTimeAccountId} 
                                    activity = {elem}
                                    userId={this.state.userId}
                                    />
                                    : null
                                    }
                                </TableCell>
                            </TableRow>
                            {/* <EditActivity show={this.state.showDialog} onClose={this.closeDialog}></EditActivity> */}
                        </>
                    ))
                }

            </>
        );
    }
}
 
export default MyActivitiesEntry;