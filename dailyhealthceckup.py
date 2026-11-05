import React, { useState } from "react";
import {
  View, Text, ScrollView, TouchableOpacity,
  StyleSheet, TextInput
} from "react-native";

export default function App() {
  const [height, setHeight] = useState("170");
  const [weight, setWeight] = useState("70");
  const [showBMI, setShowBMI] = useState(false);

  const bmi =
    Number(height) > 0 && Number(weight) > 0
      ? Number(weight) / ((Number(height) / 100) ** 2)
      : 0;

  const getCategory = () => {
    if (bmi < 18.5) return "Underweight";
    if (bmi < 25) return "Normal range";
    if (bmi < 30) return "Overweight";
    return "Obesity range";
  };

  const metrics = [
    { icon: "❤️", name: "Heart Rate", value: "72 bpm" },
    { icon: "🩸", name: "Blood Pressure", value: "120/80" },
    { icon: "🫁", name: "Oxygen Level", value: "98%" },
    { icon: "🌡️", name: "Temperature", value: "36.8°C" },
  ];

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.greeting}>Hello, User 👋</Text>
        <Text style={styles.heading}>Your Health Dashboard</Text>
        <Text style={styles.subtitle}>
          Take care of your health every day.
        </Text>
      </View>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Today's Health Status</Text>
        <Text style={styles.status}>● Health tracking dashboard</Text>
        <Text style={styles.small}>
          Sample values below. Enter your actual measurements
          to track your health.
        </Text>
      </View>

      <Text style={styles.section}>Health Metrics</Text>

      <View style={styles.grid}>
        {metrics.map((item, index) => (
          <View style={styles.metric} key={index}>
            <Text style={styles.icon}>{item.icon}</Text>
            <Text style={styles.metricName}>{item.name}</Text>
            <Text style={styles.metricValue}>{item.value}</Text>
          </View>
        ))}
      </View>

      <Text style={styles.section}>Health Services</Text>

      <TouchableOpacity
        style={styles.service}
        onPress={() => setShowBMI(!showBMI)}
      >
        <Text style={styles.serviceTitle}>⚖️ BMI Calculator</Text>
        <Text style={styles.small}>
          Calculate your Body Mass Index
        </Text>
      </TouchableOpacity>

      {showBMI && (
        <View style={styles.card}>
          <Text style={styles.cardTitle}>BMI Calculator</Text>

          <Text>Height (cm)</Text>
          <TextInput
            style={styles.input}
            keyboardType="numeric"
            value={height}
            onChangeText={setHeight}
          />

          <Text>Weight (kg)</Text>
          <TextInput
            style={styles.input}
            keyboardType="numeric"
            value={weight}
            onChangeText={setWeight}
          />

          {bmi > 0 && (
            <>
              <Text style={styles.result}>
                BMI: {bmi.toFixed(1)}
              </Text>
              <Text style={styles.status}>{getCategory()}</Text>
              <Text style={styles.small}>
                BMI is a screening measure, not a diagnosis.
              </Text>
            </>
          )}
        </View>
      )}

      <TouchableOpacity style={styles.service}>
        <Text style={styles.serviceTitle}>📅 Book Health Checkup</Text>
        <Text style={styles.small}>
          Schedule your next medical appointment
        </Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.service}>
        <Text style={styles.serviceTitle}>📄 Medical Reports</Text>
        <Text style={styles.small}>
          View your medical test reports
        </Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.service}>
        <Text style={styles.serviceTitle}>👨‍⚕️ Find a Doctor</Text>
        <Text style={styles.small}>
          Connect with healthcare professionals
        </Text>
      </TouchableOpacity>

      <Text style={styles.footer}>
        Health Checkup App © 2026
      </Text>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#F4F7FB",
  },
  header: {
    backgroundColor: "#1769AA",
    padding: 28,
    paddingTop: 60,
    borderBottomLeftRadius: 28,
    borderBottomRightRadius: 28,
  },
  greeting: {
    color: "white",
    fontSize: 17,
  },
  heading: {
    color: "white",
    fontSize: 25,
    fontWeight: "bold",
    marginTop: 12,
  },
  subtitle: {
    color: "#DCEEFF",
    marginTop: 8,
  },
  card: {
    backgroundColor: "white",
    margin: 16,
    padding: 20,
    borderRadius: 16,
    elevation: 2,
  },
  cardTitle: {
    fontSize: 19,
    fontWeight: "bold",
    marginBottom: 12,
  },
  status: {
    color: "#16834A",
    fontWeight: "bold",
    marginTop: 8,
  },
  small: {
    color: "#718096",
    marginTop: 7,
    fontSize: 13,
  },
  section: {
    fontSize: 20,
    fontWeight: "bold",
    margin: 16,
  },
  grid: {
    flexDirection: "row",
    flexWrap: "wrap",
    paddingHorizontal: 10,
  },
  metric: {
    backgroundColor: "white",
    width: "45%",
    margin: "2.5%",
    padding: 16,
    borderRadius: 15,
  },
  icon: {
    fontSize: 27,
  },
  metricName: {
    color: "#718096",
    marginTop: 10,
  },
  metricValue: {
    fontSize: 18,
    fontWeight: "bold",
    marginTop: 5,
    color: "#1769AA",
  },
  service: {
    backgroundColor: "white",
    marginHorizontal: 16,
    marginBottom: 12,
    padding: 18,
    borderRadius: 14,
  },
  serviceTitle: {
    fontSize: 17,
    fontWeight: "bold",
  },
  input: {
    borderWidth: 1,
    borderColor: "#CBD5E0",
    borderRadius: 8,
    padding: 12,
    marginVertical: 10,
  },
  result: {
    color: "#1769AA",
    fontSize: 25,
    fontWeight: "bold",
    marginTop: 10,
  },
  footer: {
    textAlign: "center",
    color: "#718096",
    margin: 30,
  },
});
