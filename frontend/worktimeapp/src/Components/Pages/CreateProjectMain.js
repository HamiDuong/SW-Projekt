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
import Card from '@mui/material/Card';
import DeveloperBoardIcon from '@mui/icons-material/DeveloperBoard';
import Typography from '@mui/material/Typography';

/**
 * @author [Esra Özkul](https://github.com/EsraOEzkul)
 */

/**
 * ProjectBOs werden hier erstellt und alle Users werden geholt.
 */
class CreateProjectMain extends Component {
    constructor(props) {
        super(props);
        //Die Änderungen werden für CreateProjectMain gespeichert.
        this.togglePopups = this.togglePopups.bind(this);
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

    /**
     * Hier wird der Popup aufgerufen.
     */
    togglePopups() {
        this.setState({
            selected: true,
        });
    }


    /**
     * Hier werden die Project Objekte erstellt und die entsprechenden API Funktionen aufgerufen.
     */
    addProjects = () => {
        let newProject = new ProjectBO(this.state.projectName, this.state.commissioner, this.props.userId);
        console.log(newProject)
        console.log(this.props.userId)
        WorkTimeAppAPI.getAPI().addProject(newProject).then(project =>
            this.setState({
                projectName: project.name,
                commissioner: project.commissioner,
                userId: 1,
                projectId: project.id,
            }, this.addProjectDurationBooking(this.state.projectId),
            )
        )
    }
    
    /**
     * Hier werden alle User Objekte geholt und in die Liste users gepsiechert.
     */
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

    /**
     * Hier werden die ProjectDuration Objekte und Booking Objekte erstellt und die entsprechenden API Funktionen aufgerufen.
     */
    addProjectDurationBooking = () => {
            let newProjectDurationBO = new ProjectDurationBO(this.state.start, this.state.end, this.state.startEvent, this.state.endEvent, this.state.type, this.state.projectId);
           console.log(newProjectDurationBO)
            WorkTimeAppAPI.getAPI().addProjectDuration(newProjectDurationBO)
               
            let newBookingBO = new BookingBO(this.state.workTimeAccountId, this.props.userId, this.state.type, this.state.eventBookingId, this.state.timeintervalBookingId)
            WorkTimeAppAPI.getAPI().addBooking(newBookingBO)
            console.log(this.state.type)
            console.log(newProjectDurationBO)
            console.log(newBookingBO)
    }
        
    /* 
    Sobald die Komponenten geladen hat sollen alle Users geholt werden.
    */
    componentDidMount(){
        this.getAllUsers();
    }

    /** Behandelt Wertänderungen der Formular-Textfelder und validiert diese */
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

    /** Im Showing wird der Text eingezeigt, wenn noch kein Projekt erstellt wurde.
    * Wenn ein Projekt erstellt wurde so wird CreateProject weitergegeben.
    */
    showing() {
        if (this.state.selected) {
            console.log('showing läuft', this.state.projectId)
            return <CreateProject onChange={this.handleChange} value={this.state.projectId} selected={true} 
            // key={users.getID()} 
            user={this.users}  /> 
            
        } else {
            return <h3>You haven´t created a project yet.</h3>
        }
    }

    /**
     * Sobald der Button 'Create Project' geklickt wird, wird die Funktion addProject aufgerufen
     * und im State wird selected true gesetzt.
     */
    handleClick() {
        this.addProjects();
        // this.addTimeIntervalBooking();
        this.setState({
            selected: true,
        });
    }

    /**
     * Öffnen des Selects für CreateProject
     */
    handleChange() {
        this.setState({
            selected: true,
        });
    }
    
    /**
     * Hier wird im State der Start DateTime gespeichert.
     */
    handleStartDateChange(newValue){
        this.setState({
            start: format(new Date(newValue), "yyyy-MM-dd HH:mm:ss")
        })
        console.log(this.state.start)
    }

    /**
     * Hier wird im State der End DateTime gespeichert.
     */
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
            <Card sx={{ m:5, p:2, minwidth: 500}}>
                <Grid container spacing={2} sx={{mb:2}} direction="row" alignItems="center">
                        <Grid item  sx={{border: 1, borderRadius: 4, ml:2, p:2}}>
                            <Grid item >
                                <DeveloperBoardIcon/>
                            </Grid>
                        </Grid>
                        <Grid item xs={12} sm={4} sx={{pb:1}}>
                            <Typography variant="h5" component="div">
                            Create Your Project.
                            </Typography>
                            <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                            Please fill out all relevant information. 
                            </Typography>
                        </Grid>
                </Grid>
                <Box
                component="form"
                sx={{
                    '& > :not(style)': { m: 1, width: '25ch' },
                }}
                noValidate
                autoComplete="off"
                >
                {/**Hier befinden sich die TextFields für das befüllen der Values, die später in der Funktion addProject aufgerufen werden. */}
                <TextField type='text' required fullWidth margin='normal' id='projectName' label='project name:' value={projectName}
                    onChange={this.textFieldValueChange} error={projectNameValidationFailed}
                    helperText={projectNameValidationFailed ? 'The project name must contain at least one character' : ' '} />
                <TextField type='text' required fullWidth margin='normal' id='commissioner' label='commissioner:' value={commissioner}
                    onChange={this.textFieldValueChange} error={commissionerValidationFailed}
                    helperText={commissionerValidationFailed ? 'The commissioner must contain at least one character' : ' '} />


                
                <LocalizationProvider dateAdapter={AdapterDateFns}>
                                <DateTimePicker
                                    style="margin-left:-1px"
                                    required fullWidth margin='normal'
                                    renderInput={(props) => <TextField {...props} />}
                                    label="Start"
                                    value={this.state.start}
                                    onChange={(newValue) => {
                                    this.handleStartDateChange(newValue);
                                    }}
                                    minDate={new Date('2022-01-01')}
                                />
                                
                            </LocalizationProvider>  
                
                <LocalizationProvider dateAdapter={AdapterDateFns}>
                                <DateTimePicker
                                    style="margin-left:-2px"
                                    margin='normal'
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
            </Card>
        );
    }
}

export default CreateProjectMain;