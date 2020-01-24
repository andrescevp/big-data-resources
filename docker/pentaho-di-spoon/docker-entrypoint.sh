#! /bin/sh
USER_HOME=/home/${DOCKER_USER}
echo "Mapping UID $TARGET_UID and GID $TARGET_GID for container user ${DOCKER_USER}..."
sed -i s/$DOCKER_USER:x:1000:1000/$DOCKER_USER:x:$TARGET_UID:$TARGET_GID/ /etc/passwd

echo "Mapping UID and GID in files..."
chown $DOCKER_USER.$DOCKER_USER /home/$DOCKER_USER

echo "Using $DISPLAY for contacting X server..."

SCRIPT=$USER_HOME/start.sh
echo "#!/bin/sh" > $SCRIPT
echo "export JAVA_HOME=$JAVA_HOME" >> $SCRIPT
echo "export DISPLAY=$DISPLAY" >> $SCRIPT
echo "export QT_GRAPHICSSYSTEM=opengl"  >> $SCRIPT
echo "cd /opt" >> $SCRIPT
echo "echo Starting spoon.sh" >> $SCRIPT
echo "./data-integration/spoon.sh" >> $SCRIPT
chmod +x $SCRIPT

echo "Starting start script..."
sudo -u $DOCKER_USER $SCRIPT