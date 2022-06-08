import React, { Component } from 'react';
import { TableCell, TableRow } from "@mui/material";
import EditActivity from './Dialog/EditActivity';


class MyActivitiesEntry extends Component {
    constructor(props) {
        super(props);
        this.state = {
            activity : props.activity,
            showDialog: false
        }
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
                    <TableCell>{this.state.activity.name}</TableCell>
                    <TableCell>{this.state.activity.capacity}</TableCell>
                    <TableCell></TableCell>
                </TableRow>
                <EditActivity show={this.state.showDialog} onClose={this.closeDialog}></EditActivity>
            </>
        );
    }
}
 
export default MyActivitiesEntry;