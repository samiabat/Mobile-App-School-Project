import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
      appBar: AppBar(
        title: Text("My first app trial"),
      ),
      body: Column(
        children: [
          Container(
            margin: EdgeInsets.all(10.0),
            child: RaisedButton(
              onPressed: () {},
              child: Text("Add Product"),
            ),
          ),
          Card(
              child: Column(
            children: <Widget>[
              Image.network(
                'https://picsum.photos/250?image=9',
              ),
              Text("This my first app that I have draw thank you every body!"),
            ],
          ))
        ],
      ),
    ));
  }
}
