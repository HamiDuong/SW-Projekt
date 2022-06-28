import React, { Component } from 'react';
import { TableCell, TableRow } from "@mui/material";
import EditActivity from './Dialog/EditActivity';
import WorkTimeAppAPI from '../API/WorkTimeAppAPI';

/**
 * Activity-Eintrag für Projekte von MyProject
 * 
 * @author [Vi Nam Le] (https://github.com/vinamle)
 */

class MyActivitiesEntry extends Component {
    constructor(props) {
        super(props);
        this.state = {
            projectId : props.projectId,
            activity : null,
            showDialog: false
        }
    }

    getActivities = () => {
        WorkTimeAppAPI.getAPI().getActivitiesByProject(this.state.projectId).then( activities =>
            this.setState({
                activity : activities
            }, function(){
                console.log("Activities aus Backend")
            })
        )
    }

    showEdit = () => {
        this.setState({
            showDialog: true
        }, function(){
            console.log("EditWindow öffnen per OnClick")
        })
    }

    closeDialog = (booking) => {
        if(booking){
            this.updateBooking(booking)
            this.setState({
                showDialog: false
            }, function(){
                console.log("Editwindow wird geschlossen")
            })
        }else{
            this.setState({
                showDialog: false
            },function(){
                console.log("Editwindow wird geschlossen ohne Update")
            })

        }
    }

    state = {  }
    render() { 
        return (
            <>
                <TableRow
                    hover
                    onClick = {this.showEdit}
                >
                    <TableCell>{}</TableCell>
                    <TableCell>{}</TableCell>
                    {/* <TableCell></TableCell> */}
                </TableRow>
                {/* <EditActivity show={this.state.showDialog} onClose={this.closeDialog}></EditActivity> */}
            </>
        );
    }
}
 
export default MyActivitiesEntry;