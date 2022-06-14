// import React, { Component } from 'react';
// import TextField from '@mui/material/TextField';
// import Box from '@mui/material/Box';
// import Button from '@mui/material/Button';
// import Grid from '@mui/material/Grid'; 
// import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
// import Dialog from '@mui/material/Dialog';
// import DialogActions from '@mui/material/DialogActions';
// import DialogContent from '@mui/material/DialogContent';
// import DialogContentText from '@mui/material/DialogContentText';
// import DialogTitle from '@mui/material/DialogTitle';
// import {Typography,InputAdornment, IconButton, MenuItem} from '@mui/material';
// import SearchIcon from '@mui/icons-material/Search';


// // // class AddMembers extends Component {
// // //     initialState = {
// // //         userName: '',
// // //         selectedUser: null,
// // //         targetUsers: [],
// // //         loadingInProgress: false,
// // //         userSearchError: null
// // //     }
// // //     constructor(props) {
// // //         super(props);

// // //         this.state = this.initialState;
// // //     }
// // //     addMember = () => { this.state.getFirstName, this.state.capacity, this.state.projectId, this.state.currentCapacity);
// // //       console.log(newActivity)
// // //       WorkTimeAppAPI.getAPI().addActivity(newActivity).then(activity => {
// // //         this.setState(this.baseState);
// // //         this.props.onClose(activity);
// // //       }).catch(e => 
// // //         this.setState({
// // //           updatingInProgress: false,
// // //           updatingError: e
// // //         })
// // //         );
// // //       this.setState({
// // //         updatingInProgress: true,
// // //         updatingError: null
// // //       });
// // //     }
// // //     searchUser = async () => {
// // //         const {userName} = this.state;
// // //         if (userName.length > 0) {
// // //             try {
// // //                 this.setState({
// // //                     targetUsers: [],
// // //                     selectedUser:null,
// // //                     loadingInProgress:true,
// // //                     userSearchError: null
// // //                 });
// // //                 const users = await WorkTimeAppAPI.getAPI().searchUser(userName);
// // //                 console.log(users)

// // //                 let selectedUser = null;

// // //                 if (users.length > 0) {
// // //                     selectedUser = users[0];
// // //                 }

// // //                 this.setState({
// // //                     targetUsers: users,
// // //                     selectedUser: selectedUser,
// // //                     loadingInProgress: false,
// // //                     userSearchError: null
// // //                 });
// // //             } catch (e){
// // //                 this.setState ({
// // //                     targetUsers: [],
// // //                     selectedUser: null,
// // //                     loadingInProgress: false,
// // //                     userSearchError: e
// // //                 });

// // //             } 
// // //             } else{
// // //                 this.setState({
// // //                     userNotFound: true
// // //                 });
// // //             }
// // //         }
// // //         /** Handles the close / cancel button click event */
// // //         handleClose = (member) => {
// // //          // Reset the state
// // //             this.setState(this.initialState);
// // //             this.props.onClose(member);
// // //         }
// // //         userSelectionChange = (event) => {
// // //             let user = event.target.value;
// // //             let selectedUser = null;
        
// // //             if (user.length > 0) {
// // //               selectedUser = user[0]
// // //             }
        
// // //             this.setState({
// // //               selectedUser: user,
              
// // //             });
// // //           }
    
// // //     render() { 
// // //         const {user} = this.props;
// // //         const {userName, targetUsers, selectedUser, userNotFound, loadingInProgress,
// // //         userSearchError} = this.state;
// // //         return ( 
// // //             <DialogTitle>
                
// // //                 {
// // //                 (targetUsers.length === 0) ?
// // //                   <TextField autoFocus fullWidth margin='normal' type='text' required id='userName' label='User name:'
// // //                     onChange={this.textFieldValueChange}
// // //                     onBlur={this.searchUser}
// // //                     error={userNotFound}
// // //                     helperText={userNotFound ? 'No user with the given name have been found' : ' '}
// // //                     InputProps={{
// // //                       endAdornment: <InputAdornment position='end'>
// // //                         <IconButton onClick={this.searchUser}>
// // //                           <SearchIcon />
// // //                         </IconButton>
// // //                       </InputAdornment>,
// // //                     }} />
// // //                     :
// // //                     <TextField select autoFocus fullWidth margin='normal' type='text' required id='userName' label='User name:'
// // //                     value={selectedUser}
// // //                     onChange={this.userSelectionChange}>
// // //                     {
// // //                       this.state.targetUsers.map((user) => (
// // //                         <MenuItem key={user.getID()} value={user}>
// // //                           {user.getLastName()}, {user.getFirstName()}
// // //                         </MenuItem>
// // //                       ))
// // //                     }
// // //                   </TextField>
// // //                     }
// // //                     <DialogActions>
// // //                       <Button onClick={this.handleClose} color='secondary'>
// // //                         Cancel
// // //                       </Button>
// // //                       <Button disable ={!selectedUser} variant='contained' color='primary' onClick={this.AddMembers}
// // //                     </DialogActions>

                    
// // //             {/* <Box
// // //             component="form"
// // //             sx={{
// // //              '& > :not(style)': { m: 1, width: '25ch' },
// // //                 }}
// // //                 noValidate
// // //                 autoComplete="off">
// // //             <div className='popup'>
// // //                 <div className='popup_inner'>
                
// // //                 <TextField id="outlined-basic" label="first name" variant="outlined" />
// // //                 <br/>
// // //                 <TextField id="outlined-basic" label="last name" variant="outlined" />
// // //                 <Grid xs={12} item>
// // //                     <Button variant="contained" onClick={this.addProject}>Add Member</Button>
// // //                 </Grid>
                
                
// // //                 <Grid xs={12} item>
// // //                     <Button variant="contained" onClick={this.props.closePopupMembers}>Close</Button>
// // //                 </Grid>


// // //             </div> 
               
// // //             </div> 
// // //          </Box>  */}
            
// // //     </DialogTitle>
// // //         );
// // //     }
// // // }
 
// // // export default AddMembers;
// // class AddMember extends Component {
// //   constructor(props) {
// //     super(props);
// //   }
// //   //Aufruf bei Abbruch
// //   handleClose = (addmmember) => {
// //     this.props.onClose(addmmember);
// //   }
// //   state = {  }
// //   render() { 
// //     return (  );
// //   }
// // }
 
// // export default AddMember;

// class AddMembers extends Component {
//   constructor(props) {
//     super(props);
 
//     this.state = { 
//       projectuser: [],
//       loadingInProgress: false,
//       showAddProjectUser: false,
//       userName :'',
//       targetProjectUser: [],
//       selectedProjectUser: null,
//    } 
// }
// getUsers = () => {
//   WorkTimeAppAPI.getAPI().getAllUsers(this.props.getID()).then(userBOs =>
//     this.setState({
//       projectuser: userBOs,
//       loadingInProgress: false,
//     })).catch (e =>
//       this.setState({
//         projectuser: [],
//         loadingInProgress: false,
//       }))
// }

// searchUser = async () => {
//   const {userName} = this.state;
//   if(userName.length > 0) {
//     try{
//       const user = await WorkTimeAppAPI.getAPI().searchUser(userName);
//       let selectedProjectUser = null;

//       if (user.length > 0) {
//         selectedProjectUser = user[0];
//       }
//       this.setState({
//         targetProjectUser: user,
//         selectedProjectUser: selectedProjectUser,
//       });
//     } catch (e){
//       this.setState({
//         targetProjectUser: [],
//         selectedProjectUser: null,
//       });
//     }
//   }
// }
// userSelectionChange = (event) => {
//   const val = event.target.value;
//   this.setState({
//     [event.target.id]: val
//   });
// }
// textFieldValueChange = (event) => {
//   const val = event.target.value;
//   this.setState({
//     [event.target.id]: val
//   });
// }
// addProjectUser = () => {
//   // Hier weiter machen. 
// }
//   render() { 
//     return (  
//       <div>
//         Hallo
//       </div>
//     );
//   }
// }
 
// export default AddMembers;
import React, { Component } from 'react';



class AddMembers extends Component {
  constructor(props) {
    super(props);
  }
  state = {  }
  render() { 
    return ( 
      <div>
        Hallo
      </div>
     );
  }
}
 
export default AddMembers;