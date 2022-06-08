import React from 'react'
import { Button } from '@mui/material'
import { Dialog, DialogTitle, DialogContent, DialogContentText, DialogActions} from '@material-ui/core';
import { useState } from 'react'
import { 
    TextField,
    List
} from '@mui/material';

export const MyProjectpopup = () => {

    function deleteProject(){
        console.log("Projekt gelöscht")
        setOpen(false)
    }

    function saveProject(){
        console.log("Projekt abspeichern")
        setOpen(false)
    }

    const [open, setOpen] = useState(false)
    return(
        <>
            <Button onClick={() => setOpen(true)}>Edit Project</Button>
            <Dialog 
                open={open}
                onCLose={() => setOpen(false)}
                aria-labelledby='dialog-title' 
                aria-describedby='dialog-description'>
                <DialogTitle id='dialog-title'>Edit Project</DialogTitle>
                <DialogContent>
                    <DialogContentText id ='dialog-description'>Change the name and duration of your project</DialogContentText>
                    <TextField
                        id="name"
                        label="Project Name"
                        variant="standard"
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <TextField
                        id="start"
                        label="Project Start"
                        variant="standard"
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <TextField
                        id="end"
                        label="Project End"
                        variant="standard"
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />

                    <List>
                        <p>Hier kommen die Activities eines Projekts welche Bearbeitet werden können</p>

                    </List>
                </DialogContent>
                <DialogActions>
                    <Button onClick={() => setOpen(false)}>Cancel</Button>
                    <Button onClick={() => deleteProject()}>Delete</Button>
                    <Button onClick={() => saveProject()}>Save Changes</Button>
                    
                </DialogActions>
            </Dialog>
        </>

    )

}