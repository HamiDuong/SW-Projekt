import React, { Component } from 'react';
import { Dialog, DialogActions, DialogContent, DialogTitle, paperClasses, TextField } from '@mui/material';
import { pickersDayClasses } from '@mui/x-date-pickers/PickersDay/pickersDayClasses';
import ProjectBO from '../../API/ProjectBO';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import CreateProject from '../CreateProjectEntry';
import ProjectDurationBO from '../../API/ProjectDurationBO';
import BookingBO from '../../API/BookingBO';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';
import { format } from "date-fns";

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
            userId: 1,
            projectId: 1,
            selected: false,
            projectNameValidationFailed: false,
            projectNameEdited: false,
            commissionerValidationFailed: false,
            commissionerEdited: false,
            filteredUsers: [],
            loadingInProgress: false,
            error: null,
            start: Date,
            end: Date,
            startEvent: null,
            endEvent: null,
            type: 'ProjectDuration',
            workTimeAccountId:0,
            event: Date,
            projectdurationId: null,
            bookingId: null,
            projectduration: null,
            workTimeAccountId: 1,
            eventBookingId: 0,
            timeintervalBookingId: 0,
            

            
        }


    }

    togglePopups() {
        this.setState({
            selected: true,
        });
    }



    addProjects = () => {
        let newProject = new ProjectBO(this.state.projectName, this.state.commissioner, this.state.userId);
        console.log(newProject)
        console.log(this.props.userId)
        WorkTimeAppAPI.getAPI().addProject(newProject).then(project =>
            this.setState({
                projectName: project.name,
                commissioner: project.commissioner,
                userId: 1,
                projectId: project.id,
            }, this.addProjectDurationBooking(),
            )
        )
        }

    // addProjects = () => {
    //     let newProject = new ProjectBO(this.state.projectName, this.state.commissioner, this.state.userId);
    //     console.log(newProject)
    //     console.log(this.props.userId)
    //     WorkTimeAppAPI.getAPI().addProject(newProject).then(project =>
    //         this.setState({
    //             projectName: project.name,
    //             commissioner: project.commissioner,
    //             userId: 1,
    //             projectId: project.id,
    //         }, function () {
    //             console.log('add project läuft')
    //         }))
    //         let newProjectDurationBO = new ProjectDurationBO(this.state.start, this.state.end, this.state.startEvent, this.state.endEvent, this.state.type, this.state.projectId);
    //         WorkTimeAppAPI.getAPI().addProjectDuration(newProjectDurationBO).then(projectduration =>
    //             this.setState({
    //                 start : projectduration.start,
    //                 end : projectduration.end,
    //                 projectduration: projectduration,
    //                 projectdurationId: projectduration.id

    //             }))
    //         let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.state.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
    //         WorkTimeAppAPI.getAPI().addBooking(newBookingBO).then(booking =>
    //             this.setState({
    //                 workTimeAccountId: 1,
    //                 userId : 1,
    //                 bookingId: booking.id,
    //             }))
   
    // }
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
    addProjectDurationBooking = () => {
            let newProjectDurationBO = new ProjectDurationBO(this.state.start, this.state.end, this.state.startEvent, this.state.endEvent, this.state.type, this.state.projectId);
           console.log(newProjectDurationBO)
            WorkTimeAppAPI.getAPI().addProjectDuration(newProjectDurationBO)
               
            let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.state.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addBooking(newBookingBO).then(booking =>
                this.setState({
                    workTimeAccountId: 1,
                    projectId: 1,
                    userId : 1,
                    type: 'PojectDuration',
                }))
            console.log(this.state.type)
            console.log(newProjectDurationBO)
            console.log(newBookingBO)
        
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
        // this.addTimeIntervalBooking();
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
    
    handleStartDateChange(newValue){
        this.setState({
            start: format(new Date(newValue), "yyyy-MM-dd HH:mm:ss")
        })
        console.log(this.state.start)
    }
    handleEndDateChange(newValue){
        this.setState({
            end: format(new Date(newValue), "yyyy-MM-dd HH:mm:ss")
        })
        console.log(this.state.end)
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
                <LocalizationProvider dateAdapter={AdapterDateFns}>
                                <DateTimePicker
                                    renderInput={(props) => <TextField {...props} />}
                                    label="Start"
                                    value={this.state.start}
                                    onChange={(newValue) => {
                                    this.handleStartDateChange(newValue);
                                    }}
                                    minDate={new Date('2022-01-01')}
                                />
                                
                            </LocalizationProvider>  
                <br />
                <LocalizationProvider dateAdapter={AdapterDateFns}>
                                <DateTimePicker
                                    renderInput={(props) => <TextField {...props} />}
                                    label="End"
                                    value={this.state.end}
                                    onChange={(newValue) => {
                                    this.handleEndDateChange(newValue);
                                    }}
                                    minDate={new Date('2022-01-01')}
                                />
                                
                            </LocalizationProvider>            

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