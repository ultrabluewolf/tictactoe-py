NAME=tictactoe
SRCS=driver.py engine.py board.py player.py validator.py
PYIM=/opt/pyinstaller-2.0/utils/Makespec.py
PYIB=/opt/pyinstaller-2.0/utils/Build.py

build: spec ${SRCS}
	${PYIB} ${NAME}.spec

spec: ${SRCS}
	${PYIM} --onefile -n ${NAME} ${SRCS}

clean:
	-rm -r *.pyc dist build logdict*.log ${NAME}.spec
