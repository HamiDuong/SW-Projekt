import React, { Component } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import WorkTimeAppAPI from './../API/WorkTimeAppAPI';
import UserBO from '../API/UserBO';

class MyProfile extends Component {
    constructor(props) {
      super(props)
      this.handleChange = this.handleChange.bind(this);
      this.state = {
          id:0,
      dateOfLastChange : 0,
       first_name:"",
       last_name:"",
       mail_adress:"",
       user_name:"",
       updatingError: null,
       updatingInProgress: false,  
      }
    }

    handleChange = (e) =>{
        this.setState({ [e.target.name] : e.target.value },
            function(){
                console.log(this.state.first_name)
            });}

    render() { 
        const {first_name, last_name, mail_adress, user_name} =this.state
        return (
        <Box
            component="form"
            sx={{'& > :not(style)': { m: 1, width: '25ch' }, }}
            noValidate
            autoComplete="off"
            >
            <TextField id="first_name" label="Outlined" variant="outlined" value={first_name} name ='first_name' onChange={this.handleChange}/>
            <TextField id="last_name" label="Outlined" variant="outlined" value={last_name} name ='last_name' onChange={this.handleChange}/>
            <TextField id="mail_adress" label="Outlined" variant="outlined" value={mail_adress} name ='mail_adress' onChange={this.handleChange}/>
            <TextField id="user_name" label="Outlined" variant="outlined" value={user_name} name ='user_name' onChange={this.handleChange}/>
            <Button variant="outlined" onClick={this.handleChange}>Speichern</Button>
            </Box>
        )

    }
}
 
export default MyProfile;
