import {
    Button,
    Dialog,
    DialogActions,
    DialogContent,
    DialogTitle,
    TableContainer,
    Table,
    TextField } from '@mui/material';
import React, { Component } from 'react';
import ProjectWorkBO from '../../API/ProjectWorkBO';
import WorkTimeAPI from '../../API/WorkTimeAppAPI'

class EditProject extends Component {
    constructor(props){
        super(props);
        this.state = {
            project : props.project,
            activity : '',

            projectname : props.project.name,
            commissioner : props.project.commissioner
        }
        this.baseState = this.state;
    }

    handleClose = () => {
        this.props.onClose(null);
    }

    deleteProject = (project) => {
        WorkTimeAPI.getAPI().deleteProject(project).then(
            this.handleClose()
        )
    }

    updateProject = () => {
        let updatedProject = Object.assign(new ProjectWorkBO(), this.state.project);
        updatedProject.setName(this.state.projectname);
        updatedProject.setCommisioner(this.state.commissioner);

        WorkTimeAPI.getAPI().updateProject(updatedProject).then(
            console.log(updatedProject)
        ).then(
            project => {
                this.baseState.projectname = this.state.projectname;
                this.baseState.commissioner = this.state.commissioner;
            }
        )
        this.handleClose();
    }

    getActivities = () => {
        WorkTimeAPI.getAPI().getActivitiesByProject(this.state.project.id).then( activities =>
            this.setState({
                activity : activities
            }, function(){
                console.log("Activities aus Backend")
            })
        )
    }
    
    render() { 
        const { classes, show } = this.props
        return (
                show ?
                <Dialog open = {show} onClose = {this.handleClose} maxWidth = 'sm'>
                    <DialogContent>
                        <DialogTitle>
                            Edit the Project
                        </DialogTitle>
                    </DialogContent>
                    <TextField
                        id="projectname"
                        label="Project Name"
                        variant="standard"
                        defaultValue={this.state.projectname}
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <TextField
                        id="commisioner"
                        label="Commisioner"
                        variant="standard"
                        defaultValue={this.state.commissioner}
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <TableContainer>
                        <Table>

                        </Table>
                    </TableContainer>
                    <DialogActions>
                        <Button
                            onClick={this.handleClose}
                        >
                            Cancel
                        </Button>
                        <Button
                            onClick={this.updateProject}
                        >
                            Save
                        </Button>
                    </DialogActions>
                </Dialog>
                :null
        );
    }
}
 
export default EditProject;