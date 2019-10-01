# alfred-menubar-timer
Use Alfred to show a simple countdown timer in macOS menu bar

## Usage

Type `t 5m` or `t break 5m` to set up a timer that shows up in menu bar:

![Screenshot of Alfred](/screenshot-a.png)

![Screenshot of menu bar](/screenshot-b.png)

Type `t stop` to stop the timer. The timer will keep on running until you stop it or set a new one. This is so that you can track how much time you ran over.

### Supported time formats

`t 10s` `t 10sec` `t 10seconds`
`t 5m` `t 5min` `t 5minutes`
`t 1h` `t 1hour`

If you want to display a name in front of the timer, put it first, like `t work 15min`.


## Installation

1. Download and open the `.alfredworkflow` file.
2. Download and install Bitbar via https://github.com/matryer/bitbar#get-started
3. Download the `simple_timer.1s.py` file and put it in the Bitbar plugins you created
