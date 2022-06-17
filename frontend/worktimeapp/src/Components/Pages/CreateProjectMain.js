import React, { Component } from 'react';
import { Dialog, DialogActions, DialogContent, DialogTitle, paperClasses, TextField } from '@mui/material';
import { pickersDayClasses } from '@mui/x-date-pickers/PickersDay/pickersDayClasses';
import ProjectBO from '../../API/ProjectBO';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import CreateProject from '../CreateProjectEntry';

class CreateProjectMain extends Component {
    constructor(props) {
        super(props);
        this.togglePopups = this.togglePopups.bind(this);
        // this.toggleMembers = this.toggleMembers.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.handleClick = this.handleClick.bind(this);

        this.state = {
            projectName: null,
            commissioner: null,
            userId: 0,
            projectId: '',
            selected: false,
            projectNameValidationFailed: false,
            projectNameEdited: false,
            commissionerValidationFailed: false,
            commissionerEdited: false,
            filteredUsers: [],
            loadingInProgress: false,
            error: null,
        }


    }

    togglePopups() {
        this.setState({
            selected: true,
        });
    }



    addProjects = () => {
        let newProject = new ProjectBO(this.state.projectName, this.state.commissioner, this.props.userId);
        console.log(newProject)
        console.log(this.props.userId)
        WorkTimeAppAPI.getAPI().addProject(newProject).then(project =>
            this.setState({
                projectName: project.name,
                commissioner: project.commissioner,
                userId: project.userId,
                projectId: project.id,
            }, function () {
                console.log('add project läuft')
            })
        )
    }
    getAllUsers = () => {
        WorkTimeAppAPI.getAPI().getAllUsers()
        .then(userBOs =>
            this.setState({
                users: userBOs,
                filteredUsers: [...userBOs],
                loadingInProgress: false,
                error: null

            })).catch( e =>
                this.setState({
                    users: [],
                    loadingInProgress: false,
                    error: e
                }));
                this.setState({
                    loadingInProgress: true,
                    error: null
                });

    }
    componentDidMount(){
        this.getAllUsers();

    }

    /** Handles value changes of the forms textfields and validates them */
    textFieldValueChange = (event) => {
        const value = event.target.value;

        let error = false;
        if (value.trim().length === 0) {
            error = true;
        }

        this.setState({
            [event.target.id]: event.target.value,
            [event.target.id + 'ValidationFailed']: error,
            [event.target.id + 'Edited']: true
        });
    }


    showing() {
        if (this.state.selected) {
            console.log('showing läuft', this.state.projectId)
            return <CreateProject onChange={this.handleChange} value={this.state.projectId} selected={true} 
            // key={users.getID()} 
            user={this.users}  /> 
            
        } else {
            return <h1>You haven´t selected a project yet.</h1>
        }
    }

    handleClick() {
        this.addProjects();
        this.setState({
            selected: true,
        });
        console.log(this.state.projectId, 'Hallooohhooo')
    }

    handleChange() {
        this.setState({
            selected: true,
        });
    }

    render() {
        const { projectName, projectNameValidationFailed, commissioner, commissionerValidationFailed } = this.state
        const func = this.showing()
        return (
            <Box
                component="form"
                sx={{
                    '& > :not(style)': { m: 1, width: '25ch' },
                }}
                noValidate
                autoComplete="off"
            >
                <TextField type='text' required fullWidth margin='normal' id='projectName' label='project name:' value={projectName}
                    onChange={this.textFieldValueChange} error={projectNameValidationFailed}
                    helperText={projectNameValidationFailed ? 'The project name must contain at least one character' : ' '} />
                <TextField type='text' required fullWidth margin='normal' id='commissioner' label='commissioner:' value={commissioner}
                    onChange={this.textFieldValueChange} error={commissionerValidationFailed}
                    helperText={commissionerValidationFailed ? 'The commissioner must contain at least one character' : ' '} />


                <br />
                <TextField
                    id="startfilter"
                    label="Duration Start"
                    variant="standard"
                    format={'YYYY/MM/DD'}
                    type="date"
                    InputLabelProps={{
                        shrink: true,
                    }}
                />
                <br />
                <TextField
                    id="startfilter"
                    label="Duration Ende"
                    variant="standard"
                    format={'YYYY/MM/DD'}
                    type="date"
                    InputLabelProps={{
                        shrink: true,
                    }}
                />

                <Grid xs={12} item>
                    <Button
                        variant="contained"
                        onClick={this.handleClick}>
                        Create Project
                    </Button>
                </Grid>

                {func}




            </Box>

        );
    }
}

export default CreateProjectMain;