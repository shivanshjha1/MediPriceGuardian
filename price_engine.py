
class PriceEngine:

    # Price-gouging threshold: 150% of market price
    PRICE_THRESHOLD = 1.5

    # -----------------------------------------
    # CALCULATE PROCEDURE COST
    # -----------------------------------------

    def calculate_estimate(self, hospital, procedure):

        surgeon_fee = procedure.surgeon_fee
        item_details = []
        missing_items = []
        total_cost = surgeon_fee

        for consumable in procedure.consumables:

            item_name = consumable.name

            if item_name not in hospital.pricing:
                missing_items.append(item_name)
                continue

            hospital_price = hospital.pricing[item_name]

            item_details.append({
                "name": item_name,
                "market_price": consumable.market_price,
                "hospital_price": hospital_price
            })

            total_cost += hospital_price

        return {
            "hospital": hospital.name,
            "procedure": procedure.name,
            "surgeon_fee": surgeon_fee,
            "items": item_details,
            "missing_items": missing_items,
            "total_cost": total_cost
        }

    # -----------------------------------------
    # CHECK PRICE GOUGING
    # -----------------------------------------

    def check_price_gouging(self, hospital, procedure):

        alerts = []

        for consumable in procedure.consumables:

            item_name = consumable.name

            if item_name not in hospital.pricing:
                continue

            market_price = consumable.market_price
            hospital_price = hospital.pricing[item_name]

            threshold_price = (
                market_price * self.PRICE_THRESHOLD
            )

            # Alert only when price is strictly above 150%
            if hospital_price > threshold_price:

                alerts.append({
                    "item": item_name,
                    "market_price": market_price,
                    "hospital_price": hospital_price,
                    "threshold_price": threshold_price
                })

        return alerts

    # -----------------------------------------
    # GENERATE INDIVIDUAL PRICE REPORT
    # -----------------------------------------

    def generate_report(self, hospital, procedure):

        estimate = self.calculate_estimate(
            hospital, procedure
        )

        alerts = self.check_price_gouging(
            hospital, procedure
        )

        print("\n========== PRICE REPORT ==========")

        print("Hospital:", estimate["hospital"])
        print("Procedure:", estimate["procedure"])

        print("\nSurgeon Fee: Rs.", estimate["surgeon_fee"])

        print("\nConsumable Price Details:")

        for item in estimate["items"]:

            print("\nItem:", item["name"])
            print("Market Price: Rs.", item["market_price"])
            print("Hospital Price: Rs.", item["hospital_price"])

        if estimate["missing_items"]:

            print("\nPrices unavailable for:")

            for item_name in estimate["missing_items"]:
                print("-", item_name)

        print("\nEstimated Total: Rs.", estimate["total_cost"])

        print("\nPrice Gouging Alerts:")

        if alerts:

            for alert in alerts:

                print("\nALERT:", alert["item"])
                print("Market Price: Rs.", alert["market_price"])
                print("150% Threshold: Rs.", alert["threshold_price"])
                print("Hospital Price: Rs.", alert["hospital_price"])
                print("Status: PRICE GOUGING DETECTED")

        else:
            print("No price gouging detected.")

        print("\n==================================")

    # -----------------------------------------
    # GENERATE OVERALL PRICE GOUGING REPORT
    # -----------------------------------------

    def generate_gouging_report(self, hospitals, procedures):

        print("\n========== OVERALL PRICE GOUGING REPORT ==========")

        total_alerts = 0

        for hospital in hospitals:

            print("\nHospital:", hospital.name)

            for procedure in procedures:

                alerts = self.check_price_gouging(
                    hospital, procedure
                )

                if alerts:

                    print("\nProcedure:", procedure.name)

                    for alert in alerts:

                        total_alerts += 1

                        print("\n  ALERT:", alert["item"])
                        print("  Market Price: Rs.", alert["market_price"])
                        print("  150% Threshold: Rs.", alert["threshold_price"])
                        print("  Hospital Price: Rs.", alert["hospital_price"])
                        print("  Status: PRICE GOUGING DETECTED")

        if total_alerts == 0:
            print("\nNo price gouging detected.")

        print("\nTotal Price Gouging Alerts:", total_alerts)
        print("Threshold: Strictly greater than 150%")
        print("==================================================")

        return total_alerts
