import React, { Component } from 'react';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid'; 
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import {Typography,InputAdornment, IconButton, MenuItem} from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';


class AddMembers extends Component {
    initialState = {
        userName: '',
        selectedUser: null,
        targetUsers: [],
        loadingInProgress: false,
        userSearchError: null
    }
    constructor(props) {
        super(props);

        this.state = this.initialState;
    }
    searchUser = async () => {
        const {userName} = this.state;
        if (userName.length > 0) {
            try {
                this.setState({
                    targetUsers: [],
                    selectedUser:null,
                    loadingInProgress:true,
                    userSearchError: null
                });
                const users = await WorkTimeAppAPI.getAPI().searchUser(userName);
                console.log(users)

                let selectedUser = null;

                if (users.length > 0) {
                    selectedUser = users[0];
                }

                this.setState({
                    targetUsers: users,
                    selectedUser: selectedUser,
                    loadingInProgress: false,
                    userSearchError: null
                });
            } catch (e){
                this.setState ({
                    targetUsers: [],
                    selectedUser: null,
                    loadingInProgress: false,
                    userSearchError: e
                });

            } 
            } else{
                this.setState({
                    userNotFound: true
                });
            }
        }
        /** Handles the close / cancel button click event */
        handleClose = (member) => {
         // Reset the state
            this.setState(this.initialState);
            this.props.onClose(member);
        }
        userSelectionChange = (event) => {
            let user = event.target.value;
            let selectedUser = null;
        
            if (user.length > 0) {
              selectedUser = user[0]
            }
        
            this.setState({
              selectedUser: user,
              
            });
          }
    
    render() { 
        const {user} = this.props;
        const {userName, targetUsers, selectedUser, userNotFound, loadingInProgress,
        userSearchError} = this.state;
        return ( 
            <DialogTitle>
                
                {
                (targetUsers.length === 0) ?
                  <TextField autoFocus fullWidth margin='normal' type='text' required id='userName' label='User name:'
                    onChange={this.textFieldValueChange}
                    onBlur={this.searchUser}
                    error={userNotFound}
                    helperText={userNotFound ? 'No user with the given name have been found' : ' '}
                    InputProps={{
                      endAdornment: <InputAdornment position='end'>
                        <IconButton onClick={this.searchUser}>
                          <SearchIcon />
                        </IconButton>
                      </InputAdornment>,
                    }} />
                    :
                    <TextField select autoFocus fullWidth margin='normal' type='text' required id='userName' label='User name:'
                    value={selectedUser}
                    onChange={this.userSelectionChange}>
                    {
                      this.state.targetUsers.map((user) => (
                        <MenuItem key={user.getID()} value={user}>
                          {user.getLastName()}, {user.getFirstName()}
                        </MenuItem>
                      ))
                    }
                  </TextField>
                    }
                
            {/* <Box
            component="form"
            sx={{
             '& > :not(style)': { m: 1, width: '25ch' },
                }}
                noValidate
                autoComplete="off">
            <div className='popup'>
                <div className='popup_inner'>
                
                <TextField id="outlined-basic" label="first name" variant="outlined" />
                <br/>
                <TextField id="outlined-basic" label="last name" variant="outlined" />
                <Grid xs={12} item>
                    <Button variant="contained" onClick={this.addProject}>Add Member</Button>
                </Grid>
                
                
                <Grid xs={12} item>
                    <Button variant="contained" onClick={this.props.closePopupMembers}>Close</Button>
                </Grid>


            </div> 
               
            </div> 
         </Box>  */}
            
    </DialogTitle>
        );
    }
}
 
export default AddMembers;