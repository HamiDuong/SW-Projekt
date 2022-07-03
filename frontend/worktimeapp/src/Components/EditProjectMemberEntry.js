import React, { Component } from 'react';
import {
    Button,
    TableRow,
    TableCell,
    TextField,
    Table} from '@mui/material';
import WorkTimeAppAPI from '../API/WorkTimeAppAPI';
import ProjectUserBO from '../API/ProjectUserBO';

class EditProjectMemberEntry extends Component {
    constructor(props){
        super(props);
        this.state = {
            user : props.user,
            projectId : props.projectId,
            showDialog : false,
            capacity : 0,
            currentProjectUser : null
        }
        this.baseState = this.state;
    }

    deleteMember = () => {
        console.log(this.state.projectId);
        console.log(this.props.projectId);
        console.log(this.state.user[0].id);
        WorkTimeAppAPI.getAPI().getProjectUserByUserId(this.state.user[0].id, this.props.projectId).then( projectuser =>
            WorkTimeAppAPI.getAPI().deleteProjectUser(projectuser.id).then( user =>
                console.log(user)    
            )
        )
        this.props.onClose(this.state.user[0])
        console.log(this.state.user[0])
    }
    
    getCurrentProjectUser = () => {
        WorkTimeAppAPI.getAPI().getProjectUserByUserId(this.state.user[0].id, this.props.projectId).then( projectuser =>
            this.setState({
                currentProjectUser : projectuser
            }, function(){
                console.log(this.state.currentProjectUser);
                console.log(projectuser)
            })
        )
    }

    getCapacity = () => {
        WorkTimeAppAPI.getAPI().getProjectUserByUserId(this.state.user[0].id, this.props.projectId).then( projectuser =>
            this.setState({
                capacity : projectuser.capacity
            }, function(){
                console.log(this.state.capacity)
            })
        )
    }


    setPropState = () => {
        this.setState({
            user : this.props.user,
            projectId : this.props.projectId
        })
    }

    componentDidMount(){
        this.getCapacity();
        this.getCurrentProjectUser();
        console.log("EditProject Member")
        console.log(this.state.user[0].lastName + ", " + this.state.user[0].firstName)
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
    handleChange = (e) =>{
        this.setState({ [e.target.name] : e.target.value })}

    updateCapacity = () => {
        let updatedProjectUserBO = Object.assign(new ProjectUserBO(), this.state.currentProjectUser);
        console.log(updatedProjectUserBO)
        updatedProjectUserBO.setCapacity(this.state.capacity);
        WorkTimeAppAPI.getAPI().updateProjectUser(updatedProjectUserBO);
        console.log(updatedProjectUserBO)
    }

    render() { 
        const {capacity} = this.state
        return (
            <>
                <TableRow
                    hover
                    onClick = {this.showDialog}
                >
                    <TableCell>
                        {this.state.user[0].lastName + ", " + this.state.user[0].firstName}
                    </TableCell>
                    <TableCell>
                        <Button
                            onClick = {this.deleteMember}
                        >
                            Delete
                        </Button>
                    </TableCell>
                </TableRow>
                <TableRow>
                    <TableCell>
                        <TextField
                            name="capacity"
                            label="Capacity"
                            onChange={this.handleChange}
                            value = {capacity}
                        >

                        </TextField>
                    </TableCell>
                    <TableCell >
                        <Button
                            onClick = {this.updateCapacity}
                        >
                            Save Change
                        </Button>
                    </TableCell>
                </TableRow>
                <TableRow>
                    <TableCell>

                    </TableCell>
                    <TableCell>
                        
                    </TableCell>
                </TableRow>
                
            </>
        );
    }
}
 
export default EditProjectMemberEntry;