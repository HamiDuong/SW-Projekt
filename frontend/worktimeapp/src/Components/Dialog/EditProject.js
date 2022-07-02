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
import ProjectBO from '../../API/ProjectBO';
import WorkTimeAPI from '../../API/WorkTimeAppAPI';
import EditProjectMemberEntry from '../EditProjectMemberEntry';

class EditProject extends Component {
    constructor(props){
        super(props);
        this.state = {
            projectId : this.props.project,
            p : '',
            members : "",
            projectmember : [],

            projectname : '',
            commissioner : ''
        }
        this.baseState = this.state;
    }

    handleClose = () => {
        this.props.onClose(null);
    }

    getProject = () => {
        WorkTimeAPI.getAPI().getProject(this.state.projectId).then( project =>
            this.setState({
                p : project,
                projectname : project.name,
                commissioner : project.commissioner
            }, function(){
                console.log("Projekt aus Backend")
            })
        )
    }

    deleteProject = (project) => {
        WorkTimeAPI.getAPI().deleteProject(project).then(
            this.handleClose()
        )
    }

    updateProject = () => {
        console.log("Update Projekt")
        let hold = document.getElementById("projectname");
        let pname = hold.value;
        let hold2 = document.getElementById("commissioner");
        let commi = hold2.value;

        let updatedProject = Object.assign(new ProjectBO(), this.state.p);
        updatedProject.setName(pname);
        updatedProject.setCommissioner(commi);

        WorkTimeAPI.getAPI().updateProject(updatedProject).then(
            console.log(updatedProject)
        ).then(
            project => {
                this.baseState.projectname = pname;
                this.baseState.commissioner = commi;
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

    handleChange = ev => {
        this.setState({ [ev.target.name]: ev.target.value });
    };

    getProjectMembers = () => {
        console.log("Projekt ID", this.state.projectId);
        WorkTimeAPI.getAPI().getMembersByProjectId(this.state.projectId).then( members =>
            this.setState({
                members : members
            }, function(){
                members.forEach(elem => {
                    WorkTimeAPI.getAPI().getUserById(elem.userId).then( user =>
                           this.setState({
                                projectmember : [...this.state.projectmember, user]
                           }, function(){
                                console.log("PROJEKTMEMBER")
                                console.log(this.state.projectmember);
                           })
                    )
                });
            })    
        )
    }

    componentDidMount(){
        this.getProject();
        this.getProjectMembers();
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
                        id="commissioner"
                        label="Commisioner"
                        variant="standard"
                        defaultValue={this.state.commissioner}
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <TableContainer>
                        <Table>
                            {
                                this.state.projectmember.map((user) => (
                                    <EditProjectMemberEntry user = {user}></EditProjectMemberEntry>
                                ))
                            }

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