import React, { Component } from 'react';
import {
    Button,
    TableRow,
    TableCell} from '@mui/material';

class EditProjectMemberEntry extends Component {
    constructor(props){
        super(props);
        this.state = {
            user : props.user
        }
        this.baseState = this.state;
    }

    componentDidMount(){
        console.log("EditProject Member")
        console.log(this.state.user)
    }

    render() { 
        return (
            <TableRow>
                <TableCell>
                    {}
                </TableCell>
                <TableCell>
                    <Button>
                        Delete
                    </Button>
                </TableCell>
            </TableRow>
        );
    }
}
 
export default EditProjectMemberEntry;