#!/bin/sh
echo "Access-Control-Allow-Origin: *"
echo "Content-type: application/json"
echo ""

PASSWORD="openwrt"
SCRIPT="gpio/script/gpio.sh"

#KEY=`echo "$QUERY_STRING" | sed -n 's/^.*key=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
#echo "KEY IS= $KEY"
#exit 0

KEY=`echo "$QUERY_STRING" | sed -n 's/^.*key=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
AUTH=`echo "$QUERY_STRING" | sed -n 's/^.*auth=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
TOGGLE=`echo "$QUERY_STRING" | sed -n 's/^.*toggle=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
SINGLE=`echo "$QUERY_STRING" | sed -n 's/^.*single=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
GROUP=`echo "$QUERY_STRING" | sed -n 's/^.*group=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
ALLON=`echo "$QUERY_STRING" | sed -n 's/^.*allon=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
ALLOFF=`echo "$QUERY_STRING" | sed -n 's/^.*alloff=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
LIST=`echo "$QUERY_STRING" | sed -n 's/^.*list=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
STATUS=`echo "$QUERY_STRING" | sed -n 's/^.*status=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
LISTJADWAL=`echo "$QUERY_STRING" | sed -n 's/^.*listjadwal=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
UPDATENAMA=`echo "$QUERY_STRING" | sed -n 's/^.*updtaenama=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
TARGET=`echo "$QUERY_STRING" | sed -n 's/^.*target=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
STATUS=`echo "$QUERY_STRING" | sed -n 's/^.*status=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
NAMA=`echo "$QUERY_STRING" | sed -n 's/^.*nama=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`


	
#	if [ $KEY = $PASSWORD ]
#	then
#	 echo "PASSWORD ANDA BENAR"
#	else
#	echo "PASSWORD SALAH<br>"
#	 echo "KEY = $KEY"
#	fi

if [[ $AUTH ]]
then
# outp=`bash $SCRIPT toggle $TARGET`
 echo '{ "success": true, "message": "sukses login!" }';
#echo $outp
 exit 0
fi

if [[ $TOGGLE ]]
then
 outp=`bash $SCRIPT toggle $TARGET`
 echo $outp
 exit 0
fi

if [[ $SINGLE ]]
then
 outp=`bash $SCRIPT single $TARGET $STATUS`
 echo $outp
 exit 0
fi

if [[ $GROUP ]]
then
 outp=`bash $SCRIPT toggle $TARGET $STATUS`
 echo $outp
 exit 0
fi

if [[ $ALLON ]]
then
 outp=`bash $SCRIPT allon`
 echo $outp
 exit 0
fi

if [[ $ALLOFF ]]
then
 outp=`bash $SCRIPT alloff`
 echo $outp
 exit 0
fi


if [[ $LIST ]]
then
 outp=`bash $SCRIPT list`
 echo $outp
 exit 0
fi

if [[ $STATUS ]]
then
 outp=`bash $SCRIPT status`
 echo $outp
 exit 0
fi

if [[ $LISTJADWAL ]]
then
 outp=`bash $SCRIPT list-jadwal`
 echo $outp
 exit 0
fi

if [[ $UPDATENAMA ]]
then
 outp=`bash $SCRIPT update-nama $NAMA`
 echo $outp
 exit 0
fi
#echo '<html>'
#echo '<head>'
#echo '<title>Test CGI Bro</title>'
#echo '</head>'
#echo "<body>$DTA  tes cgi script bro...yup..yup"
#echo "<br>PASSWORDNYA $PASSWORD<br>"
#echo "Query = $KEY <br>"
#echo '</body>'
#echo '</html>'
#exit 0

echo $QUERY_STRING

# echo '{ "success": false, "message": "request tidak lengkap atau salah" }'; 
