// import { Dialog, DialogActions, DialogContent, DialogTitle, paperClasses, TextField } from '@mui/material';
// import { pickersDayClasses } from '@mui/x-date-pickers/PickersDay/pickersDayClasses';
// import React, { Component } from 'react';
// import ProjectBO from '../API/ProjectBO';
// import ActivityBO from '../API/ActivityBO';
// import WorkTimeAppAPI from '../API/WorkTimeAppAPI';
// import Box from '@mui/material/Box';
// //import TextField from '@mui/material/TextField';
// import Button from '@mui/material/Button';
// import Grid from '@mui/material/Grid'; 
// import AddActivities from './Dialog/AddActivities';
// import AddMembers from './Dialog/AddMembers';
// import PropTypes from 'prop-types';
// import Typography from '@mui/material/Typography';
// import CreateProject from './CreateProject';
// import AddIcon from '@mui/icons-material/Add';

// class CreateProjectEntry extends Component {
//     constructor(props) {
//         super(props);
    
//     this.state = { 
//         //CreateProject
//         projectName: null,
//         commissioner: null,
//         projectNameValidationFailed: false,
//         projectNameEdited: false,
//         commissionerValidationFailed: false,
//         commissionerEdited: false,
//         userid: 0,

//         //AddActivity
//         activitylist : [],
//         activityName: null,
//         capacity: null,
//         activitytNameValidationFailed: false,
//         activityNameEdited: false,
//         capacityValidationFailed: false,
//         capacityEdited: false,
//         projectId: 0,
//         currentCapacity: 0,
//         showAddActivities: false,

//         //AddMember
//         firstName: null,
//         lastName: null,
//         loadingInProgress: false,
//         selectedProjectUser: null,
//         showAddMembers: false,
        
//     };
//     }   
//     //Methoden für CreateProject
//     addProjects = () => { 
//         let newProject = new ProjectBO(this.state.projectName, this.state.commissioner, this.state.userid);
//         console.log(newProject)
//         WorkTimeAppAPI.getAPI().addProject(newProject).then(project => {
//           this.setState(this.baseState);
//           this.props.onClose(project);
//         }).catch(e => 
//           this.setState({
//             updatingInProgress: false,
//             updatingError: e
//           })
//           );
//         this.setState({
//           updatingInProgress: true,
//           updatingError: null
//         });
//       }
//     /** Handles value changes of the forms textfields and validates them */
//     textFieldValueChange = (event) => {
//         const value = event.target.value;
    
//         let error = false;
//         if (value.trim().length === 0) {
//           error = true;
//         }
    
//         this.setState({
//           [event.target.id]: event.target.value,
//           [event.target.id + 'ValidationFailed']: error,
//           [event.target.id + 'Edited']: true
//         });
//         }
      
        
        
//         //Aufruf, wenn der AddActivities Button geklickt wurde, vom AddActivities
//         addActivitiesButtonclicked = (event) => {
//             event.stopPropagation();
//             this.setState({
//             showAddActivities: true
//             });
//         }

//         //Schließen des Dialogs, onclose von AddMember Dialog
//         closeAddActivitiesDialog = (addActivity) => {
//             this.setState({
//                 showAddActivities: false
//             });
//         }
    
//         addMembersButtonclicked = (event) => {
//             event.stopPropagation();
//             this.setState({
//             showAddMembers: true
//             });
//         }

//         //Schließen des Dialogs, onclose von AddMember Dialog
//         closeAddMembersDialog = (addMember) => {
//             this.setState({
//                 showAddMembers: false
//             });
//         }
//         addActivityFormClosed = activity => {
//           // customer is not null and therefore created
//           if (activity) {
//             console.log(activity)
//             const newActivityList = [...this.state.activitylist, activity];
//             this.setState({
//               activitylist: newActivityList,
//               showAddActivities: false
//             });
//           } else {
//             this.setState({
//               showAddActivities: false
//             });
//           }
//         }
    


     
//     render() { 
//         const {classes} = this.props; 
//         const {projectName, projectNameValidationFailed, commissioner, commissionerValidationFailed} = this.state
//         return ( 
//             // Methoden für CreateProject/AddProject
//             <Box component="form" sx={{'& > :not(style)': { m: 1, width: '25ch' }, }} noValidate autoComplete="off"> 

//             <TextField type='text' required fullWidth margin='normal' id='projectName' label='project name:' value={projectName} 
//             onChange={this.textFieldValueChange} error={projectNameValidationFailed} 
//             helperText={projectNameValidationFailed ? 'The project name must contain at least one character' : ' '} />
//             <TextField type='text' required fullWidth margin='normal' id='commissioner' label='commissioner:' value={commissioner}
//             onChange={this.textFieldValueChange} error={commissionerValidationFailed}
//             helperText={commissionerValidationFailed ? 'The commissioner must contain at least one character' : ' '} />
              
//             <br/>

//             <TextField
//             id="startfilter"
//             label="Duration Start"
//             variant="standard"
//             format={'YYYY/MM/DD'}
//             type = "date"
//             InputLabelProps={{
//             shrink: true,
//                         }}
//             />

//             <br/>

//             <TextField
//             id="startfilter"
//             label="Duration Ende"
//             variant="standard"
//             format={'YYYY/MM/DD'}
//             type = "date"
//             InputLabelProps={{
//             shrink: true,
//                         }}
//             />
//             <Grid xs={12} item>
//                     <Button 
//                     variant="contained" 
//                     onClick={this.addProjects}>
//                       Create Project
//                       </Button>
//             </Grid>
//             {/* Methoden für Activity */}
//             <Button variant='contained' color='primary' startIcon={<AddIcon/>} onClick={this.addActivitiesButtonclicked}>
//                 Add Activity
//             </Button>
//             <AddActivities show={this.state.showAddActivities} 
//             addActivty = {this.addActivity} textFieldValueChange={this.textFieldValueChange}
//             activityName = {this.state.activityName} capacity= {this.state.capacity}
//             onClose = {this.addActivityFormClosed}/>
//             <br/>
            
//             <Button variant='contained' color='primary' startIcon={<AddIcon/>} onClick={this.addMembersButtonclicked}>
//             Add Member
//             </Button>

//             <AddMembers show={this.state.showAddMembers} 
//             addMember = {this.addMember} textFieldValueChange={this.textFieldValueChange}
//             firstName = {this.state.firstName} lastName= {this.state.lastName}
//             onClose = {this.closeAddMembersDialog}/>
            
//             </Box>

        
//          );
//     }
// }
 
// export default CreateProjectEntry;