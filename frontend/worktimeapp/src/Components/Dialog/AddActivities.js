import React, { Component } from 'react';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid'; 
import ActivityBO from '../../API/ActivityBO';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import { Dialog, DialogActions, DialogContent, DialogTitle, IconButton} from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';



class AddActivities extends Component {
    constructor(props) {
        super(props);
        this.state={
            activityName: null,
            capacity: null,
            activitytNameValidationFailed: false,
            activityNameEdited: false,
            capacityValidationFailed: false,
            capacityEdited: false,
            projectId: '',
            currentCapacity: 0,
    }
    this.baseState = this.state;
}

    addActivity = () => { 
        let newActivity = new ActivityBO(this.state.activityName, this.state.capacity, this.props.projectId, this.state.currentCapacity);
        console.log(newActivity)
        WorkTimeAppAPI.getAPI().addActivity(newActivity).then(activity => 
         this.setState({
          activityName:activity.name,
          capacity: activity.capacity,
          currentCapacity: activity.currentCapacity,
          projectId: activity.project_id
         }, 
         function(){
          console.log('Here', activity, this.state.projectId, this.state.activityName)
         }))
      }

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
    
    render() { 
        const {activityName, activityNameValidationFailed, capacity, capacityValidationFailed} = this.state 
        return ( 
           <Box
            component="form"
             sx={{
             '& > :not(style)': { m: 1, width: '25ch' },
                }}
            noValidate
            autoComplete="off">
            <div className='popup'>
                <div className='popup_inner'>
                
                <TextField type='text' required fullWidth margin='normal' id='activityName' label='activity name:' value={activityName} 
                onChange={this.textFieldValueChange} error={activityNameValidationFailed} 
                helperText={activityNameValidationFailed ? 'The activity name must contain at least one character' : ' '} />
                <TextField type='text' required fullWidth margin='normal' id='capacity' label='capacity:' value={capacity}
                onChange={this.textFieldValueChange} error={capacityValidationFailed}
                helperText={capacityValidationFailed ? 'The commissioner must contain at least one character' : ' '} />
                
                <Grid xs={12} item>
                    
                    <Button 
                    variant="contained" 
                    onClick={this.addActivity}>
                      Create Activity
                      </Button>
                    
                </Grid> 
                <br/>

                    <Grid xs={12} item>
                    <Button variant="contained" onClick={this.props.closePopupActivities}>Close</Button>
                </Grid>
                </div>
               
            </div>
            </Box>
         );
    }
}

 
export default  AddActivities;

// class AddActivites extends Component {
//   constructor(props) {
//     super(props);
//     this.state={
//         loadingInProgress: false,
//         createprojectError: null,
//         activityName: '',
//         capacity:0,
//         activitytNameValidationFailed: false,
//         activityNameEdited: false,
//         capacityValidationFailed: false,
//         capacityEdited: false,
//         projectId: 0,
//         currentCapacity: 0,
//           }
//           this.baseState = this.state;
//   }
  

//   addActivity = () => { 
//     let newActivity = new ActivityBO(this.state.activityName, this.state.capacity, this.state.projectId, this.state.currentCapacity);
//     console.log(newActivity)
//     WorkTimeAppAPI.getAPI().addActivity(newActivity).then(activity => {
//         this.setState(this.baseState);
//         console.log('TEst')
//         this.props.onClose(activity);
//       }).catch(e => 
//         this.setState({
//           updatingInProgress: false,
//           updatingError: e
//         })
//         );
//       this.setState({
//         updatingInProgress: true,
//         updatingError: null
//       });
//     }

//   handleClose = (activity) => {
//     this.setState(this.state)
//     this.props.onClose(activity);
//   }

//   handleChange = (e) =>{
//     this.setState({ [e.target.name] : e.target.value });}

//   /** Handles value changes of the forms textfields and validates them */
//   textFieldValueChange = (event) => {
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
  
//   render() { 
//     const {show, } = this.props
//     const {activityName, activityNameValidationFailed, capacity, capacityValidationFailed} = this.state 
//     return ( 
    
    
//       <Dialog open={this.props.show} onClose={this.handleClose} maxWidth='md'>
//         <DialogTitle id='from-dialog-title'>
//           <IconButton sx={{ position: 'absolute', right: 1, top:1, color:'grey[500]'}} onClick={this.handleClose}>
//             <CloseIcon/>
//           </IconButton>
//           <br/>
//           Add activities to your project!
//         </DialogTitle>
//         <DialogContent>
//           <form sx={{width: '100%'}} noValidate autoComplete='off'
//            onSubmit={this.addActivity}
//           >

//               <TextField type='text'  fullWidth margin='normal'  id='activityName' label='activity name:' value={activityName} 
//                 onChange={this.handleChange} error={activityNameValidationFailed} 
//                 helperText={activityNameValidationFailed ? 'The activity name must contain at least one character' : ' '} 
//               />
//               <TextField type='text'  fullWidth margin='normal' id='capacity' label='capacity:' value={capacity}
//                 onChange={this.handleChange}  error={capacityValidationFailed}
//                 helperText={capacityValidationFailed? 'capacity must contain at least one character' : ' '} />
 
          
//           </form>
//         </DialogContent>
//         <DialogActions>
//               <Button type="submit" variant="contained" color="primary" size="large" onClick={this.addActivity}
//               >
//                         Create Activity 
//               </Button>
//               <Button onClick={this.handleClose}>Cancel</Button>
//         </DialogActions>
//       </Dialog>
//     )
//       {/* <Box
//             component="form"
//              sx={{
//              '& > :not(style)': { m: 1, width: '25ch' },
//                 }}
//             noValidate
//             autoComplete="off">
//             <div className='popup'>
//                 <div className='popup_inner'>
                
//                 <TextField type='text' required fullWidth margin='normal' id='activityName' label='activity name:' value={activityName} 
//                 onChange={this.textFieldValueChange} error={activityNameValidationFailed} 
//                 helperText={activityNameValidationFailed ? 'The activity name must contain at least one character' : ' '} />
//                 <TextField type='text' required fullWidth margin='normal' id='capacity' label='capacity:' value={capacity}
//                 onChange={this.textFieldValueChange} error={capacityValidationFailed}
//                 helperText={capacityValidationFailed ? 'The commissioner must contain at least one character' : ' '} />
                
//                 <Grid xs={12} item>
                    
//                     <Button 
//                     variant="contained" 
//                     onClick={this.addActivity}>
//                       Create Activity
//                       </Button>

//                     </Grid> 
//                     <Grid xs={12} item>
//                     <Button variant="contained" onClick={this.props.closePopupActivities}>Close</Button>
//                 </Grid>
//                 </div>
               
//             </div>
//              </Box> */}
          
//      ;
//   }
// }
 
// export default AddActivites;