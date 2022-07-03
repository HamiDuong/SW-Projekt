import React, { Component } from 'react';
import TableCell from '@mui/material/TableCell';
import TableRow from '@mui/material/TableRow';
import EditBooking from './Dialog/EditBooking'

/**
 * @author Ha Mi Duong (https://github.com/HamiDuong)
 * 
 * Erstellung eines Eintrags für Intervalbuchungen
 */
class MyBookingsIntervalEntry extends Component {
    constructor(props) {
        super(props);
        this.state = {
            booking: this.props.booking,
            showDialog: false,
            loadingInProgress: false,
            error: null,
        }
    }

    // Dialog für die Bearbeitung öffnen
    showEdit = () => {
        this.setState({
            showDialog: true
        }, function () {
            console.log("EditWindow öffnen per OnClick");
        })
    }

    // Dialog für die Bearbeitung schließen
    closeEditDialog = (booking) => {
        if (booking) {
            this.setState({
                booking: booking,
                showDialog: false
            }, function () {
                console.log("Editwindow wird geschlossen")
                console.log(this.state.booking)
                this.props.onClose1(booking)
            })
        } else {
            this.setState({
                showDialog: false
            }, function () {
                console.log("Editwindow wird geschlossen ohne Update")
            })

        }
    }

    // Debugging sobald die Komponente geladen ist
    componentDidMount() {
        console.log("Eintrag von Interval", this.props.key)
        console.log(this.state.booking)
    }



    // Änderungen in den gerenderten Komponenten im State abspeichern
    handleChange = ev => {
        this.setState({ [ev.target.name]: ev.target.value });
    };

    render() {
        const { booking } = this.state
        return (
            <>
                <TableRow
                    hover
                    onClick={this.showEdit}
                >
                    <TableCell>Interval</TableCell>
                    <TableCell>{this.state.booking.type}</TableCell>
                    <TableCell>{this.state.booking.start}</TableCell>
                    <TableCell>{this.state.booking.end}</TableCell>

                </TableRow>
                <EditBooking show={this.state.showDialog} onClose={this.closeEditDialog} booking={booking} />
            </>
        );
    }
}

export default MyBookingsIntervalEntry;