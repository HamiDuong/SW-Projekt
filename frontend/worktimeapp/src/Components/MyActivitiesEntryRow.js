import React, { Component } from 'react';
import { Button, Dialog, TableCell, TableRow, DialogContent } from "@mui/material";
import EditActivity from './Dialog/EditActivity';
import MyProjectsEntry from './MyProjectsEntry'
import WorkTimeAPI from '../API/WorkTimeAppAPI';
import DeleteActivity from './Dialog/DeleteActivity';

class MyActivitiesEntryRow extends Component {
    constructor(props) {
        super(props);
        this.togglePopupMyProjectsEntry = this.togglePopupMyProjectsEntry.bind(this);
        this.state = {
            activity : props.activity,
            showPopupMyProjectEntry: false,
            userId : props.userId,
            showWorkDialog : false,
            showDeleteActivityDialog: false,
        }
    }

    togglePopupMyProjectsEntry() {
        this.setState({
          showPopupMyProjectEntry: !this.state.showPopupMyProjectEntry
        });
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
    closeDialog = (activity) => {

        if(activity){
            this.setState({
                activity: activity,
                showWorkDialog: false
              });
        }else{
        this.setState({
            showWorkDialog: false
        }, function(){
            console.log("Editwindow wird geschlossen")
        });
       }
    }

    deleteActivityButtonClicked = () => {
        this.setState({
          showDeleteActivityDialog: true
        });
      }

    deleteActivityDialogClosed= (activity) => {
        if (activity) {
          this.props.onActivityDeleted(activity);
        };
    
        // Don´t show the dialog
        this.setState({
          showDeleteActivityDialog: false
        });
      }
    

    render() { 
        return (
            <>
                <TableRow
                    hover
                    
                >
                    <TableCell>{this.state.activity.name}</TableCell>
                    <TableCell>{this.state.activity.capacity}</TableCell>
                    <TableCell>
                        <Button variant="contained" onClick={this.togglePopupMyProjectsEntry.bind(this)}>start</Button>
                        <Button variant="contained"color="error" style={{margin:5}} onClick={this.deleteActivityButtonClicked}>Delete</Button>
                        <Button variant="contained" color="info" onClick={this.showEdit}> Edit</Button>
                        {this.state.showPopupMyProjectEntry ? 
                        <MyProjectsEntry
                        text='Close'
                        closePopup={this.togglePopupMyProjectsEntry.bind(this)}
                        // user={this.state.currentUser} workTimeAccount = {this.state.workTimeAccountId} 
                        activity = {this.state.activity}
                        userId={this.state.userId}
                        />
                        : null
                        }
                    </TableCell>
                </TableRow>
                <EditActivity show = {this.state.showWorkDialog} onClose = {this.closeDialog} activity = {this.state.activity}></EditActivity>
                <DeleteActivity show = {this.state.showDeleteActivityDialog} onClose = {this.deleteActivityDialogClosed} activity = {this.state.activity}></DeleteActivity>

            </>
        );
    }
}
 
export default MyActivitiesEntryRow;