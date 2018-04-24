import de.voidplus.myo.*;
import oscP5.*;
import netP5.*;

OscP5 oscP5;
NetAddress dest;
Myo myo;
ArrayList<ArrayList<Integer>> sensors;

void setup() {
  size(800, 400);
  background(255);
  noFill();
  stroke(0);
  // ...

  //myo = new Myo(this, true); // true, with EMG data
  
  //sensors = new ArrayList<ArrayList<Integer>>();
  //for (int i=0; i<8; i++) {
  //  sensors.add(new ArrayList<Integer>()); 
  //}
    oscP5 = new OscP5(this,12000);
  dest = new NetAddress("127.0.0.1",6449);
  frameRate(90);
}
  


void draw() {
  background(255);
  // ...
  
  // Drawing:
  synchronized (this) {
    for (int i=0; i<8; i++) {
      /*if (!sensors.get(i).isEmpty()) {
        beginShape();
        for (int j=0; j<sensors.get(i).size(); j++) {
          vertex(j, sensors.get(i).get(j)+(i*50));
        }
        endShape();
      } *b/
    }
  }
  
}

// ----------------------------------------------------------
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

void oscEvent(OscMessage theOscMessage) {
 if (theOscMessage.checkAddrPattern("/wek/outputs")==true) {
     if(theOscMessage.checkTypetag("f")) { // looking for 1 control value
        theOscMessage.print();
        float simpleMove = theOscMessage.get(0).floatValue();
     } else {
        println("Error: unexpected OSC message received by Processing: ");
        theOscMessage.print();
      }
 }
}