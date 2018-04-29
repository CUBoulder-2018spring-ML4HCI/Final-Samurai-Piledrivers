import de.voidplus.myo.*;
import oscP5.*;
import netP5.*;
import java.util.Queue;
import java.util.ArrayDeque;

OscP5 oscP5;
OscP5 oscP52;
NetAddress dest;
NetAddress dest2;
Queue<Float> queue1 = new ArrayDeque(1024);
Queue<Float> queue2 = new ArrayDeque(1024);
Myo myo;
ArrayList<ArrayList<Integer>> sensors;

void setup() {
  size(800, 400);
  background(255);
  noFill();
  stroke(0);
  // ...
  myo = new Myo(this, true); // true, with EMG data
  
  sensors = new ArrayList<ArrayList<Integer>>();
  for (int i=0; i<8; i++) {
    sensors.add(new ArrayList<Integer>()); 
  }
  
  //myo = new Myo(this, true); // true, with EMG data
  
  //sensors = new ArrayList<ArrayList<Integer>>();
  //for (int i=0; i<8; i++) {
  //  sensors.add(new ArrayList<Integer>()); 
  //}
  oscP5 = new OscP5(this,6449);
  dest = new NetAddress("127.0.0.1",6448);
  dest2 = new NetAddress("127.0.0.1",6451);
  oscP52 = new OscP5(this,12000);
  frameRate(90);
  sendOscNames();
  
  
  
  
}
  


void draw() {
  background(255);
  // ...
  
  // Drawing:
  synchronized (this) {
    for (int i=0; i<8; i++) {
      if (!sensors.get(i).isEmpty()) {
        beginShape();
        for (int j=0; j<sensors.get(i).size(); j++) {
          vertex(j, sensors.get(i).get(j)+(i*50));
        }
        endShape();
      } 
    }
  }
  
}

// ----------------------------------------------------------
void sendOscNames() {
  OscMessage msg = new OscMessage("/wekinator/control/setOutputNames");
  msg.add("move"); //Now send all 5 names
  oscP5.send(msg, dest);
}

void oscEvent(OscMessage theOscMessage) {
  
 if (theOscMessage.checkAddrPattern("/wek/output")==true) {
   
     if(theOscMessage.checkTypetag("f")) { // looking for 1 control value
       
        
        float simpleMove = theOscMessage.get(0).floatValue();
        queue1.add(simpleMove);
        int one=0;
        int two=0;
        int three=0;
        int four=0;
        for(int i=0; i<queue1.size();i++){
         float t = queue1.remove();
         if(t==1){
           one++;
         }
         if(t==2){
           two++;
         }
         if(t==3){
           three++;
         }
         if(t==4){
           four++;
         }
         queue2.add(t);
          
        }
        
        
         float val = 0;
         if(one>=two && one>=three && one>=four){
           val = 1.0;
         }
         else if(two>=one && two>=three && two>=four){
           val = 2.0;
         }
         else if(three>=one && three>=two && three>=four){
           val = 3.0;
         }
         else if(four>=one && four>=two && four>=three){
           val = 4.0;
         }
        
        
        OscMessage msg = new OscMessage("/wek/output");
        msg.add(val);
        println("Sending OSC msg: ");
        msg.print();
        oscP52.send(msg,dest2);
        
        
     } else{
        println("Error: unexpected OSC message received by Processing: ");
        theOscMessage.print();
      }
 }
}

void myoOnEmgData(Device myo, long timestamp, int[] data) {
  // println("Sketch: myoOnEmgData, device: " + myo.getId());
  // int[] data <- 8 values from -128 to 127
   OscMessage msg = new OscMessage("/wek/inputs");
   for (int i = 0; i<data.length; i++){
     msg.add((float)data[i] * 10);
   }
     oscP5.send(msg, dest);
     
     synchronized (this) {
    for (int i = 0; i<data.length; i++) {
      sensors.get(i).add((int) map(data[i], -128, 127, 0, 50)); // [-128 - 127]
     
    }
    while (sensors.get(0).size() > width) {
      for(ArrayList<Integer> sensor : sensors) {
        sensor.remove(0);
      }
    }
}
}
