import React, { Component } from 'react';
import { Button, Dialog, TableCell, TableRow, DialogContent } from "@mui/material";
import EditActivity from './Dialog/EditActivity';
import MyProjectsEntry from './MyProjectsEntry'
import WorkTimeAPI from '../API/WorkTimeAppAPI';

class MyActivitiesEntryRow extends Component {
    constructor(props) {
        super(props);
        this.togglePopupMyProjectsEntry = this.togglePopupMyProjectsEntry.bind(this);
        this.state = {
            activity : props.activity,
            showPopupMyProjectEntry: false,
            userId : props.userId,
            showWorkDialog : false
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
    closeDialog = () => {
        this.setState({
            showWorkDialog: false
        }, function(){
            console.log("Editwindow wird geschlossen")
        })
    }

    render() { 
        return (
            <>
                <TableRow
                    hover
                    onClick = {this.showEdit}
                >
                    <TableCell>{this.state.activity.name}</TableCell>
                    <TableCell>{this.state.activity.capacity}</TableCell>
                    <TableCell>
                        <Button variant="contained" onClick={this.togglePopupMyProjectsEntry.bind(this)}>start</Button>
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
            </>
        );
    }
}
 
export default MyActivitiesEntryRow;