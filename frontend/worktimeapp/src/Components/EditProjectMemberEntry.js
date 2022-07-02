import React, { Component } from 'react';
import {
    Button,
    TableRow,
    TableCell} from '@mui/material';
import WorkTimeAppAPI from '../API/WorkTimeAppAPI';

class EditProjectMemberEntry extends Component {
    constructor(props){
        super(props);
        this.state = {
            user : "",
            projectId : "",
            showDialog : false
        }
        this.baseState = this.state;
    }

    deleteMember = () => {
        WorkTimeAppAPI.getAPI().getProjectUserByUserId(this.state.projectId, this.state.user[0].getId()).then( projectuser =>
            console.log("ProjektUser gelöscht", projectuser)
        )
    }

    setPropState = () => {
        this.setState({
            user : this.props.user,
            projectId : this.props.projectId
        })
    }

    componentDidMount(){
        this.setPropState()
        console.log("EditProject Member")
        console.log(this.state.user[0].getLastName() + ", " + this.state.user[0].getFirstName())
    }

    showDialog = () => {
        this.setState({
            showDialog: true
        }, function(){
            console.log("EditWindow öffnen per OnClick");
        })        
    }

    closeDialog = (projectuser) => {
        if(projectuser){
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

    render() { 
        return (
            <>
                <TableRow
                    hover
                    onClick = {this.showDialog}
                >
                    <TableCell>
                        {this.state.user[0].getLastName() + ", " + this.state.user[0].getFirstName()}
                    </TableCell>
                    <TableCell>
                        <Button
                            onClick = {this.showDialog}
                        >
                            Delete
                        </Button>
                    </TableCell>
                </TableRow>
                <EditProjectUser show = {this.state.showDialog} onClose = {this.closeDialog} projectuser = {this.state.user}></EditProjectUser>
            </>
        );
    }
}
 
export default EditProjectMemberEntry;