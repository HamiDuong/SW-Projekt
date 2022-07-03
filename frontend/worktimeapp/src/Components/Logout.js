import React, { Component, createRef } from 'react';
import { Popover, IconButton, ClickAwayListener,Typography, Paper, Button, Grid, Divider } from '@mui/material';
import firebase from 'firebase/app';
import {signOut } from "firebase/auth";
import {auth} from '../firebaseConfig.js';
import Avatar from '@mui/material/Avatar';

class Logout extends Component {

  #avatarButtonRef = createRef();

  constructor(props) {
    super(props);

    this.state = {
      open: false,
    }
  }

  
  handleAvatarButtonClick = () => {
    this.setState({
      open: !this.state.open
    });
  }

  handleClose = () => {
    this.setState({
      open: false
    });
  }

  
  handleSignOutButtonClicked = () => {
    signOut(auth);
  }

  /** Renders the profile drop down if a loggin user is given as a prop */
  render() {
    const {user } = this.props;
    const { open } = this.state;

    return (
      user ?
        <div>
          <IconButton ref={this.#avatarButtonRef} onClick={this.handleAvatarButtonClick}>
            <Avatar src={user.photoURL} />
          </IconButton>

          <Popover open={open} anchorEl={this.#avatarButtonRef.current} onClose={this.handleClose}
            anchorOrigin={{
              vertical: 'top',
              horizontal: 'left',
            }}
            transformOrigin={{
              vertical: 'top',
              horizontal: 'right',
            }}>
            <ClickAwayListener onClickAway={this.handleClose}>
              <Paper >
                <Typography align='center'>Worktimeapp</Typography>
                <Divider/>
                <Typography align='center' variant='body2'>{user.displayName}</Typography>
                <Divider/>
                <Grid container justify='center'>
                  <Grid item>
                    <Button color='primary' onClick={this.handleSignOutButtonClicked}>Logout</Button>
                  </Grid>
                </Grid>
              </Paper>
            </ClickAwayListener>
          </Popover>
        </div>
        : null
    )
  }
}

export default Logout;

